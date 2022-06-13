import time
import pygame
import random

from mutagen.mp3 import MP3
from os import listdir
from os.path import isfile, join
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

MUSIC_FOLDER_PATH = "C:/Users/Eren/Music"
MUSIC_FOLDER_NAME = "Music"

IS_MUTED = False
IS_PAUSED = True
SHUFFLE = False
REPEAT = False
VOLUME_LEVEL = 0.7
CURRENT_POS = 0
TRACK_LENGTH = 0
IS_PLAY_TIME_ACTIVE = 0
BACKGROUND_COLOR = "#FFFFF0"
WIDTH = 435
HEIGHT = 410


def check_event():
    for event in pygame.event.get():
        if event.type == TRACK_END_EVENT:
            Next()
            break

    root.after(250, check_event)


def onselect(evt):
    Play()


def slide(ev):
    if abs(CURRENT_POS - my_slider.get()) > 1.1:
        try:
            mixer.music.set_pos(my_slider.get())
        except:
            mixer.music.load(f"{MUSIC_FOLDER_PATH}/{songs_list.get(ACTIVE)}")
            mixer.music.play(loops=0, start=my_slider.get())


def addsongs():
    temp_song = filedialog.askopenfilenames(
        initialdir=f"{MUSIC_FOLDER_NAME}/",
        title="Choose a song",
        filetypes=(("mp3 Files", "*.mp3"),),
    )

    for s in temp_song:
        s = s.replace(f"{MUSIC_FOLDER_PATH}/", "")
        songs_list.insert(END, s)


def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])


def play_time():
    if not IS_PAUSED:
        left_counter["text"] = time.strftime(
            "%M:%S", time.gmtime(int(my_slider.get()) + 1)
        )
        my_slider.set(my_slider.get() + 1)

        global CURRENT_POS
        CURRENT_POS = my_slider.get()
    root.after(1000, play_time)


def Play():
    global IS_PAUSED
    IS_PAUSED = False

    if not songs_list.curselection():
        songs_list.activate(0)
    song = f"{MUSIC_FOLDER_PATH}/{songs_list.get(ACTIVE)}"
    mixer.music.load(song)
    before_playing_new_track(track_path=song)
    mixer.music.play()
    play_pause_button["image"] = PAUSE_IMAGE
    play_pause_button["command"] = Pause


def shuffle_unshuffle():
    global SHUFFLE
    SHUFFLE = not SHUFFLE
    if SHUFFLE:
        shuffle_button["image"] = SHUFFLE_IMAGE


def before_playing_new_track(track_path: str):
    song_data = MP3(track_path)
    my_slider["to"] = song_data.info.length
    global TRACK_LENGTH
    TRACK_LENGTH = song_data.info.length
    my_slider.set(0)
    right_counter["text"] = time.strftime("%M:%S", time.gmtime(TRACK_LENGTH))
    left_counter["text"] = time.strftime("%M:%S", time.gmtime(int(my_slider.get())))


def play_track(track_name: str):
    global IS_PAUSED
    IS_PAUSED = False
    mixer.music.unload()
    track_path = f"{MUSIC_FOLDER_PATH}/{track_name}"
    before_playing_new_track(track_path=track_path)
    mixer.music.load(track_path)
    mixer.music.play()
    play_pause_button["image"] = PAUSE_IMAGE
    play_pause_button["command"] = Pause


def Pause():
    global IS_PAUSED
    IS_PAUSED = True
    mixer.music.pause()
    play_pause_button["image"] = PLAY_IMAGE
    play_pause_button["command"] = Resume


def Resume():
    global IS_PAUSED
    IS_PAUSED = False
    mixer.music.unpause()
    play_pause_button["image"] = PAUSE_IMAGE
    play_pause_button["command"] = Pause


def Previous():
    global IS_PAUSED
    IS_PAUSED = False
    mixer.music.unload()
    previous_one = songs_list.curselection()[0] - 1

    if previous_one < 0:
        previous_one = songs_list.size() - 1

    track_path = f"{MUSIC_FOLDER_PATH}/{songs_list.get(previous_one)}"
    before_playing_new_track(track_path=track_path)
    mixer.music.load(track_path)
    mixer.music.play()

    songs_list.selection_clear(0, END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)


def Next():
    mixer.music.unload()
    next_one = songs_list.curselection()[0] + 1

    if next_one == songs_list.size():
        next_one = 0

    if SHUFFLE:
        next_one = random.randint(0, songs_list.size() - 1)

    track_path = f"{MUSIC_FOLDER_PATH}/{songs_list.get(next_one)}"
    before_playing_new_track(track_path=track_path)
    mixer.music.load(track_path)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)


def set_vol(val):
    global VOLUME_LEVEL
    VOLUME_LEVEL = float(val) / 20.0
    mixer.music.set_volume(VOLUME_LEVEL)


def mute_unmute():
    global IS_MUTED
    if IS_MUTED:
        mixer.music.set_volume(VOLUME_LEVEL)
        IS_MUTED = False
        volume_button["image"] = VOLUME_IMAGE
    else:
        mixer.music.set_volume(0)
        IS_MUTED = True
        volume_button["image"] = MUTE_IMAGE


root = Tk()
root.title("Python MP3 Music Player App")
root.config(bg=BACKGROUND_COLOR)
root.geometry("{}x{}".format(WIDTH, HEIGHT))
root.minsize(width=WIDTH, height=HEIGHT)
root.maxsize(width=WIDTH, height=HEIGHT)
pygame.init()
mixer.init()

NEXT_IMAGE = PhotoImage(file="images/next_img.png")
PREV_IMAGE = PhotoImage(file="images/prev_img.png")
PLAY_IMAGE = PhotoImage(file="images/play_img.png")
PAUSE_IMAGE = PhotoImage(file="images/pause_img.png")
VOLUME_IMAGE = PhotoImage(file="images/vol.png")
MUTE_IMAGE = PhotoImage(file="images/mute.png")
SHUFFLE_IMAGE = PhotoImage(file="images/shuffle.png")

songs_list = Listbox(
    root,
    selectmode=SINGLE,
    bg=BACKGROUND_COLOR,
    fg="green",
    font=("arial", 15),
    height=12,
    width=33,
    selectbackground="green",
    selectforeground="yellow",
    borderwidth=0,
    selectborderwidth=0,
)
songs_list.grid(row=0, padx=35, columnspan=18, sticky=W)

songs_list.bind("<<ListboxSelect>>", onselect)  # '<Double-1>'

style = ttk.Style()
style.configure("TScale", background=BACKGROUND_COLOR)

previous_button = Button(
    root,
    image=PREV_IMAGE,
    command=Previous,
    bg=BACKGROUND_COLOR,
    fg="green",
    borderwidth=0,
)
previous_button.grid(row=1, column=0, sticky=W)

play_pause_button = Button(
    root, image=PLAY_IMAGE, command=Play, bg=BACKGROUND_COLOR, fg="green", borderwidth=0
)
play_pause_button.grid(row=1, column=1, sticky=W)

next_button = Button(
    root, image=NEXT_IMAGE, command=Next, bg=BACKGROUND_COLOR, fg="green", borderwidth=0
)
next_button.grid(row=1, column=2, sticky=W)

volume_button = Button(
    root,
    image=VOLUME_IMAGE,
    fg="green",
    bg=BACKGROUND_COLOR,
    command=mute_unmute,
    borderwidth=0,
)
volume_button.grid(row=1, column=3, sticky=W)

shuffle_button = Button(
    root,
    image=SHUFFLE_IMAGE,
    fg="green",
    bg=BACKGROUND_COLOR,
    command=shuffle_unshuffle,
    borderwidth=0,
)
shuffle_button.grid(row=1, column=5, padx=15, sticky=E)

scale = ttk.Scale(
    root, from_=1, to=20, orient=HORIZONTAL, command=set_vol, style="TScale"
)

scale.set(14)
scale.grid(row=1, column=4, sticky=E)
mixer.music.set_volume(VOLUME_LEVEL)

my_slider = ttk.Scale(
    root, from_=0, to=0, orient=HORIZONTAL, command=slide, length=300, style="TScale"
)
my_slider.grid(row=2, column=1, columnspan=6, sticky=W)

left_counter = Label(
    root, text="00:00", bg=BACKGROUND_COLOR, fg="green", font=("arial", 12)
)
right_counter = Label(
    root, text="00:00", bg=BACKGROUND_COLOR, fg="green", font=("arial", 12)
)

left_counter.grid(row=2, column=0, sticky=E)
right_counter.grid(row=2, column=5, sticky=W)


onlyfiles = [
    f for f in listdir(MUSIC_FOLDER_PATH) if isfile(join(MUSIC_FOLDER_PATH, f))
]

for file in onlyfiles:
    if file.endswith(".mp3"):
        songs_list.insert(END, file)

songs_list.activate(0)
songs_list.selection_set(0)

TRACK_END_EVENT = pygame.USEREVENT + 1
mixer.music.set_endevent(TRACK_END_EVENT)

check_event()
play_time()
mainloop()
