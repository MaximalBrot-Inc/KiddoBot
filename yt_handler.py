import os
import discord
import command_handler
from pytube import YouTube

dir_path = os.path.dirname(os.path.realpath("C:\_FSST\Jaeger\Shooting Range\KiddoBot"))


async def downloadvideo(link, ctx):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    name = youtubeObject.title()
    try:
        await youtubeObject.download()
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.mp4'):
                    print(root + '/' + str(file))


        #await ctx.send(find(name, path="C:\_FSST\Jaeger\Shooting Range\KiddoBot"))

    except:
        await ctx.send('HAAAAAAALT STOP! Der Link ist nicht von YouTube!!')
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