#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-28 19:55:52
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-30 03:05:54

from tkinter import filedialog, messagebox
from pytube import YouTube
from tkinter import *
import  requests

from MyThread import MyThread

# ws.mainloop()
def downloadVideo():
    if(popUpMessage("Do you want to download this video")):
        thread = MyThread(function = lambda: downloadThread())
        thread.start()


def downloadThread():
    youtube = YouTube(data.get())
    dir = filedialog.askdirectory()
    # streams = youtube.streams.filter(progressive=True)
    youtubevideo = youtube.streams.get_by_resolution("720p")
    size = youtubevideo.filesize
    message = f"Downloading {youtube.title}"
    messagesize =  f"of size {round(size/1000000, 2)}Mb"
    createLabel(message, fontsize=7)
    createLabel(messagesize, fontsize=7)
    youtubevideo.download(dir)
    messagebox.showinfo(message="Download completed")

def popUpMessage(message):
    choice = messagebox.askquestion(message=message)
    if(choice == "yes"):
        return True
    return False

def createButton(title):
    Button(window, text=title, width=20, background="red", foreground="white", 
    command=lambda: downloadVideo()).pack(pady=20)

def createLabel(message, fontsize=14):
    Label(window, text=message, font=f'san-serif {fontsize}').pack()

def createEntryBox():
    Entry(window, width=90, textvariable=data).pack()

def main():
    createLabel("Video Downloader")
    createEntryBox()
    createButton("Download")

    
window = Tk()
data = StringVar()
# window.geometry("600x400")
window.resizable(True, True)
window.title("Video Downloader")
main()
window.mainloop()

