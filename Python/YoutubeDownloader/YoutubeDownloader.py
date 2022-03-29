# Importing the youtube library {pip install pytube}
from pytube import YouTube

link = input("Enter your youtube url: ")
yt = YouTube(link)
# streams all the format available for youtube.
videos = yt.streams.all()

# Make a list pf all videos starting wit h position zero
video = list(enumerate(videos))

# This will print all the available format of the video with proper index.
count = 0
for i in videos:
    print(count, " ", i)
    count += 1

print("Enter the desired option to download the format")
# Asks user his for his format preference.
dn_option = int(input("Enter the option: "))
dn_video = videos[dn_option]
# Downloads the video
dn_video.download()

print("Downloaded successfully")

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# if __name__ == '__main__':
