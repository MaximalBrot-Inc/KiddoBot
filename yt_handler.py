import os
import discord
from pytube import YouTube, exceptions


def path():
    os.makedirs("downloaded_videos", exist_ok=True)
    return "downloaded_videos"


async def downloadvideo(link, ctx):
    try:

        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        name = youtubeObject.title

        await youtubeObject.download(output_path=path())
        #for root, dirs, files in os.walk(dir_path):
        #    for file in files:
        #       if file.endswith('.mp4'):
        #          print(root + '/' + str(file))

        #await ctx.send(find(name, path="C:\_FSST\Jaeger\Shooting Range\KiddoBot"))

    except exceptions.RegexMatchError:
        await ctx.send('HAAAAAAALT STOP! Das ist kein Link!')
    except exceptions.VideoUnavailable:
        await ctx.send('Das Video ist nicht verfügbar :(')
    await ctx.send("Fertiiiig :333")


#def Download(link):
#   youtubeObject = YouTube(link)
#  youtubeObject = youtubeObject.streams.get_highest_resolution()
# try:
#    youtubeObject.download()
#    except:
#       print("An error has occurred")
#  print("Download is completed successfully")


#link = input("Enter the YouTube video URL: ")
#Download(link)



