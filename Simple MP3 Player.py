from tkinter import filedialog
from tkinter import *
import os
from pygame import mixer

root = Tk()
root.config(bg="darkgrey")

listbox = Listbox(width=60, height=10, bg="lightblue")
paused = False

def load():
    directory = filedialog.askdirectory()
    os.chdir(directory)
    song_list = os.listdir()
    pos = 1

    for song in song_list:
        listbox.insert(1, song)
        pos += 1

def play():
    mixer.init()
    mixer.music.load(listbox.get(listbox.curselection()))
    mixer.music.play()

def pause():
    global paused

    if paused == False:
        mixer.music.pause()
        paused = True

    elif paused == True:
        mixer.music.unpause()
        paused = False

def stop():
    mixer.music.stop()

load_button = Button(text="load", width=10, bg="green", command=load)
load_button.pack(side="left")

play_button = Button(text="play", width=10, bg="lightgreen", command=play)
play_button.pack(side="bottom")

pause_button = Button(text="pause", width=10, bg="lightgreen", command=pause)
pause_button.pack(side="bottom")

stop_button = Button(text="stop", width=10, bg="red", command=stop)
stop_button.pack(side="right")

listbox.pack(side="right")

root.mainloop()