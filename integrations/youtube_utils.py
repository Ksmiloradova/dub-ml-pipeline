from pytube import YouTube

def youtube_download(link):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution().download()
    return video
