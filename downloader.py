from pytube import YouTube
from pytube import Playlist
import os

class Downloader():
    def video(self, url, only_audio, dir_name):
        vid = YouTube(url)
        print(vid.title)
        if not only_audio:
            vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="video\\"+dir_name)
        else:
            audio = vid.streams.filter(only_audio=True).first()
            out_path = audio.download(output_path="music\\"+dir_name)
            new_name = os.path.splitext(out_path)
            os.rename(out_path, new_name[0] + ".mp3")
        print("Done!!")

    def playlist(self, url,only_audio):
        playlist = Playlist(url)
        output_path_dir = playlist.title
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        if not only_audio:
            for video in playlist.videos:
                video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="video\\" + str(output_path_dir))
        else:
            for video in playlist.videos:
                audio = video.streams.filter(only_audio=True).first()
                out_path = audio.download(output_path="music\\" + str(output_path_dir))
                new_name = os.path.splitext(out_path)
                os.rename(out_path,new_name[0] + ".mp3")
        print("Done!!")