from pytube import YouTube
from pytube import Playlist
import os

class Downloader():
    def video(self, url, only_audio, dir_name):
        vid = YouTube(url)
        print(vid.title)
        if not only_audio:
            try:
                vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="video\\"+dir_name)
                self.downloaded(vid.title)
            except FileExistsError:
                self.file_exist(vid.title)
        else:
            try:
                audio = vid.streams.filter(only_audio=True).first()
                out_path = audio.download(output_path="music\\"+dir_name)
                new_name = os.path.splitext(out_path)
                os.rename(out_path, new_name[0] + ".mp3")
                self.downloaded(vid.title)
            except FileExistsError:
                os.remove(new_name[0] + '.mp4')
                self.file_exist(vid.title)

    def playlist(self, url,only_audio, dir_name):
        playlist = Playlist(url)
        output_path_dir = playlist.title
        output_path_dir = "".join(c for c in output_path_dir if c.isalnum())
        if dir_name != '':
            dir_name = dir_name + "\\" + str(output_path_dir)
        else:
            dir_name = output_path_dir
        print('Album name: ' + output_path_dir + ' Number of videos in playlist: ' + str(len(playlist.video_urls)) + '\n')
        if not only_audio:
            try:
                for video in playlist.videos:
                    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="video\\" + dir_name)
                self.downloaded(playlist.title)
            except FileExistsError:
                self.file_exist(playlist.title)
        else:
            try:
                for video in playlist.videos:
                    audio = video.streams.filter(only_audio=True).first()
                    out_path = audio.download(output_path="music\\" + dir_name)
                    new_name = os.path.splitext(out_path)
                    os.rename(out_path,new_name[0] + ".mp3")
                self.downloaded(playlist.title)
            except FileExistsError:
                os.remove(out_path)
                self.file_exist(playlist.title)

    def file_exist(self, name):
        print("File or playlist exist: " + str(name))

    def downloaded(self, name):
        print("Downloaded " + str(name))
