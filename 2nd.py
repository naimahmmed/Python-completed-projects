#modules import
from cProfile import label
import tkinter as tk
from tkinter import *
from turtle import width
from pytube import YouTube
from tkinter import filedialog, messagebox


def create_widgets():
    link_label = Label(win, text="YouTube Link :",bg="#07eff7")
    link_label.grid(row=1, column=0, pady=5, padx=5)


    win.label_text = Entry(win, width=53, textvariable=video_link)
    win.label_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(win, text="destination :",bg="#07aab0")
    destination_label.grid(row=2, column=0, padx=5, pady=5)

    win.destination_text = Entry(win, width=30, textvariable=download_path)
    win.destination_text.grid(row=2, column=1,padx=3,pady=3)

    browse_button = Button(win, text= "Choose directory", width=20, command=browse, bg="green")
    browse_button.grid(row=2, column=2, padx=2, pady=2)

    download_button = Button(win, text="Download", width=15, command=download,bg="green")
    download_button.grid(row=3, column=2, padx=2, pady=2) 



def browse():
    download_dir = filedialog.askdirectory(initialdir="choose a directory for save")
    download_path.set(download_dir)


def download():
    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_streams = get_video.streams.get_highest_resolution()
    get_streams.download(folder)

    messagebox.showinfo("Success!!", "Download has been completed!\n your file is at"+folder)
    



win = tk.Tk()
win.title("YouTube Video downloader")
win.geometry("600x200")
win.resizable(height=False, width=False)
win.config(bg="black")

video_link = StringVar()
download_path = StringVar()

create_widgets()

win.mainloop()





