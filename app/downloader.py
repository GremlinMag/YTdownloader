from pytube import YouTube
from pytube import Playlist
import os

class Downloader():
    def video(self, url, only_audio, dir_name):
        vid = YouTube(url)
        print(vid.title)
        if not only_audio:
            try:                                                                                    # download mp4 video
                vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="video\\"+dir_name)
                self.downloaded(vid.title)                                                          # print success message
            except FileExistsError:
                self.file_exist(vid.title)                                                          # print file exist message
        else:
            try:
                audio = vid.streams.filter(only_audio=True).first()                                 # select first video for download
                out_path = audio.download(output_path="music\\"+dir_name)                           # download mp4 with only audio
                new_name = os.path.splitext(out_path)                                               # remove path to new file, leave only name file
                os.rename(out_path, new_name[0] + ".mp3")                                           # rename file from mp4 to mp3
                self.downloaded(vid.title)                                                          # print success message
            except FileExistsError:
                os.remove(new_name[0] + '.mp4')
                self.file_exist(vid.title)                                                          # print file exist message

    def playlist(self, url,only_audio, dir_name):
        playlist = Playlist(url)
        output_path_dir = "".join(c for c in playlist.title if c not in "\"'\/:*?<>|")              # check album name and delete dangerous chars
        if dir_name != '':
            dir_name = dir_name + "\\" + str(output_path_dir)                                       # combine output directory
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
