import youtube_dl #scaricare la youtuble_dl
import shutil, os

link = input("inserisci il link della canzone \n")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(([link]))
try:
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            shutil.move(file, r"C:\Users\Admin\Desktop\canzoni") #scegliere la cartella dove mettere
                                                                 #la canzone
except:
    print("file già esistente")
    os.remove(file)


