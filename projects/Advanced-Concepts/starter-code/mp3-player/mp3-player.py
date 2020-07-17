# Importing Required Modules & libraries
import tkinter as tk
import pygame
import os


# Defining MusicPlayer Class
class MusicPlayer:


  # Defining Constructor
  def __init__(self,root):

    #The top level widget is called the root (Tk())
    self.root = root
    # Title of the window
    self.root.title("Music Player")
    # Window Geometry
    self.root.geometry("1000x200+200+200")

    # START CODING HERE
    # 1. Initiate pygame

    # 2. Initiate pygame mixer

    # 3. Set self.track to a tk.StringVar()
    #   NOTE: self.track will be what song is playing
    #   We want to use a StringVar() because we will use
    #   self.track to display the track name as a label
    #   For more info, http://effbot.org/tkinterbook/label.htm

    # 4. Set self.status to a tk.StringVar()
    #   NOTE: self.status will be the status of the track
    #   For example, if the song is playing the status would
    #   be "Playing"

    # Creates a track frame for song label & status label
    trackframe = tk.LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    # Inserts song track label
    songtrack = tk.Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
    # Inserts status label
    trackstatus = tk.Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
    # creating button frame
    buttonframe = tk.LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)

    # Inserts play button
    playbtn = tk.Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
    # Inserts pause button
    playbtn = tk.Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
    # Inserts unpause button
    playbtn = tk.Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
    # Inserts stop button
    playbtn = tk.Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)

    # Creates playlist frame
    songsframe = tk.LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)
    # Inserts scrollbar
    scrol_y = tk.Scrollbar(songsframe,orient=tk.VERTICAL)
    # Inserts playlist listbox
    self.playlist = tk.Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=tk.SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=tk.GROOVE)
    # Applies scrollbar to listbox
    scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=tk.BOTH)

    # 5. Paste the path to the music directory here
    os.chdir("<YOUR_PATH_TO_MUSIC")

    # 6. Set variable "songtracks" to the contents of the music directory

    # 7. Create a loop that adds each file in the music directory
    #   to self.playlist using .insert(END,track_name)
    #   To learn more, http://effbot.org/tkinterbook/listbox.htm

  # Defines play song function
  def playsong(self):

    # Sets track to the selected track
    self.track = self.playlist.get(tk.ACTIVE)

    # 8. Set status to "Playing"

    # 9. Load track to pygame mixer

    # 10. Play track using pygame mixer

  # Defines stop song function
  def stopsong(self):

    # 11. Set status to "Stopped"

    # 12. Stop song

  # Defines pause song function
  def pausesong(self):

    # 13. Set status to "Paused"

    # 14. Pause song

  # Defines unpause function
  def unpausesong(self):

    # 15. Set status to "Playing"

    # 16. Unpause music

# Creating TK Container
root = tk.Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
