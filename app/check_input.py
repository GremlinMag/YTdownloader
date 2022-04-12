from app.downloader import Downloader

downloader = Downloader()
class Check_input():
    def check_file(self, url, only_audio):
        f = open(url, "r")
        videos = f.read()
        videos = videos.split()
        dir_name = url.split(".")
        for vid in videos:
            downloader.video(vid, only_audio, dir_name[0])
        print("All done")

    def check_params(self, url, only_audio):
        if url.find("txt") != -1:
            self.check_file(url, only_audio)
        elif url.find("playlist") == -1:
            downloader.video(url, only_audio, '')
        else:
            downloader.playlist(url, only_audio)