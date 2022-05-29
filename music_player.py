from click import command
from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(50.0)

#functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/Music",title="Please select a file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green",text=str(song_title))
        volume_label.config(fg="green",text="Volume: "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Error playing track")

def reduce_volume():
    try:
        global current_volume
        if current_volume < 10:
            volume_label.config(fg="red", text="Volume: Muted")
            return
        current_volume = current_volume - float(10.0)
        current_volume =round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text= "Volume: "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.conifg(fg="red",text="Track hasn't been selected yet")
 
def increase_volume():
    try:
        global current_volume
        if current_volume > 90:
            volume_label.config(fg="green", text="Volume: Max")
            return
        current_volume = current_volume + float(10.0)
        current_volume =round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text= "Volume: "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.conifg(fg="red",text="Track hasn't been selected yet")
 

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.conifg(fg="red",text="Track hasn't been selected yet")
  

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.conifg(fg="red",text="Track hasn't been selected yet")


#Main screen
master = Tk()
master.title("Music player")

#labels
Label(master,text="Custom Music Player", font=("Calibri",15),fg="red").grid(sticky="N",row=0,padx=120)

Label(master,text="Please select a music track you would like to play", font=("Calibri",12),fg="blue").grid(sticky="N",row=1)

Label(master,text="Volume", font=("Calibri",12),fg="red").grid(sticky="N",row=4)

song_title_label=Label(master, font=("Calibri",15))
song_title_label.grid(stick="N",row=3)

volume_label = Label(master, font=("Calibri",12))
volume_label.grid(sticky="N",row = 5)


#buttons
Button(master, text="Select Song", font=("Calibri",12),command=play_song).grid(row=2,sticky="N")
Button(master, text="Pause", font=("Calibri",12),command=pause).grid(row=3,sticky="E")#one Ease very right
Button(master, text="Resume", font=("Calibri",12),command=resume).grid(row=3,sticky="W")
Button(master, text="-", font=("Calibri",12),width=5,command=reduce_volume).grid(row=5,sticky="W")
Button(master, text="+", font=("Calibri",12),width=5,command=increase_volume).grid(row=5,sticky="E")

master.mainloop()