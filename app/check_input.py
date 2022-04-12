from app.downloader import Downloader

downloader = Downloader()
class Check_input():
    def check_file(self, url, only_audio):
        f = open(url, "r")
        videos = f.read()
        videos = videos.split()
        dir_name = url.split(".")
        for vid in videos:
            self.check_params(vid, only_audio, dir_name[0])
        print("Download from .txt complete")

    def check_params(self, url, only_audio, dir_name):
        if url.find("txt") != -1:
            self.check_file(url, only_audio)
        elif url.find("playlist") != -1:
            downloader.playlist(url, only_audio, dir_name)
        else:
            downloader.video(url, only_audio, dir_name)