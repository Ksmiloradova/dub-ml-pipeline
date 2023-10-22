from pytube import YouTube


def youtube_download(link):
    yt = YouTube(link)
    print('start downloading video')
    video = yt.streams.first().download()
    print('video downloaded - ', video)
    return video
