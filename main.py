from pytube import YouTube
from sys import argv


# ensures we get the second argument which is the link
link = argv[1]

# creates YouTube object
youtube_link = YouTube(link)

# allows you to filter based on the type of stream you desire, got the highest resolution
# on a single file that allows me to combine the audio and video
youtube_download = youtube_link.streams.get_highest_resolution()

# downloads the stream into the path folder
youtube_download.download('/Users/salhinlanghi/Desktop/Offline Videos')
