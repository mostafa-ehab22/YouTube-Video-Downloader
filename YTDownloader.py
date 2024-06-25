from pytube import YouTube
from sys import argv
"""
Running program: python YTDownloader.py "LINK"
"""

# Takes 1st line after program name & stores it as link
link = argv[1]
yt = YouTube(link)

print("Title:",yt.title)
print("Views:","{:,}".format(yt.views))


# Getting Video Resolution
resolution_480 = yt.streams.filter(res="480p",progressive=True).first()

# Checking if wanted resolution available
if resolution_480:
    resolution_480.download("D:\Mostafa\YT Videos")
    print("Download Successful!")
else:
    print("Stream not availabe")