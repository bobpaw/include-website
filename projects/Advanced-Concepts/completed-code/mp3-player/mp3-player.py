# Importing Required Modules & libraries
import tkinter as tk
import pygame
import os


# Defining MusicPlayer Class
class MusicPlayer:
  # Defining Constructor
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Music Player")
    # Window Geometry
    self.root.geometry("1000x200+200+200")
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = tk.StringVar()
    # Declaring Status Variable
    self.status = tk.StringVar()
    # Creating Track Frame for Song label & status label
    trackframe = tk.LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    # Inserting Song Track Label
    self.songtrack = tk.Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Status Label
    trackstatus = tk.Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
    # Creating Button Frame
    buttonframe = tk.LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)
    # Inserting Play Button
    playbtn = tk.Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Pause Button
    playbtn = tk.Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
    # Inserting Unpause Button
    playbtn = tk.Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
    # Inserting Stop Button
    playbtn = tk.Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
    # Creating Playlist Frame
    songsframe = tk.LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)
    # Inserting scrollbar
    scrol_y = tk.Scrollbar(songsframe,orient=tk.VERTICAL)
    # Inserting Playlist listbox
    self.playlist = tk.Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=tk.SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=tk.GROOVE)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=tk.BOTH)
    # Changing Directory for fetching Songs
    os.chdir("C:\\Users\\adiso\\github\\include-website\\projects\\Advanced-Concepts\\completed-code\\mp3-player\\music")
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(tk.END,track)
  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(tk.ACTIVE))
    # Displaying Status
    self.status.set("Playing")
    # Loading Selected Song
    pygame.mixer.music.load(self.playlist.get(tk.ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()
  def stopsong(self):
    # Displaying Status
    self.status.set("Stopped")
    # Stopped Song
    pygame.mixer.music.stop()
  def pausesong(self):
    # Displaying Status
    self.status.set("Paused")
    # Paused Song
    pygame.mixer.music.pause()
  def unpausesong(self):
    # Displaying Status
    self.status.set("Playing")
    # Playing back Song
    pygame.mixer.music.unpause()
# Creating TK Container
root = tk.Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
