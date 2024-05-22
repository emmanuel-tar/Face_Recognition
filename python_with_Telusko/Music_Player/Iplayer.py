import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
#from PIL import ImageTK, Image

root = Tk()

root.title('Iplayer')
root.geometry('920x600+290+85')
root.configure(background='#212121')
root.resizable(False,False)
mixer.init()


#----------------------------
#function to open music file
#----------------------------

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)


        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

#ICON ON THE APP

image_icon = PhotoImage(fil='play_1.png')
#image_icon = ImageTK.PhotoImage(Image.open('ones.png'))

root.iconphoto(False,image_icon)

Top = PhotoImage(file='two.png')
Label(root, image=Top, bg='#0f1a2b').pack()


#logo
Logo = PhotoImage(file='log1.jpg')
Label(root,image=Logo, bg='#0f1a2b',bd=0).place(x=70, y=115)


#BUTTONS

ButtonPlay = PhotoImage(file='play.png')
Button(root,image=ButtonPlay,bg='#0f1a2b',
       bd=0,command=PlayMusic).place(x=100,y=400)

ButtonStop = PhotoImage(file='stop-button.png')
Button(root,image=ButtonStop,bg='#0f1a2b',
       bd=0,command=mixer.music.stop).place(x=30,y=500)

ButtonResume = PhotoImage(file='play.png')
Button(root,image=ButtonResume,bg='#0f1a2b',
       bd=0,command=mixer.music.unpause).place(x=115,y=500)

ButtonPause = PhotoImage(file='pause.png')
Button(root,image=ButtonPause,bg='#0f1a2b',
       bd=0,command=mixer.music.pause).place(x=200,y=500)

#LABEL
Menu = PhotoImage(file='log2.jpg')
Label(root,image=Menu,bg='#0f1a2b').pack(padx=10,pady=50,side=RIGHT)


Frame_Music = Frame(root,bd=2, relief=RIDGE)
Frame_Music.place(x=330, y=350, width=560,height=250)

Button(root,text='Open Folder',width=15, height=2,
       font=('times new roman', 12,'bold'),
       fg='black', bg='#21b3de',command=AddMusic).place(x=330,y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music,width=100,font=('Times new roman',10),bg='#333333',fg='grey',selectbackground='lightblue', cursor='hand2',
                   bd=0,yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()


