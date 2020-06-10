import tkinter
from pygame import mixer
import sounddevice as sd
from scipy.io.wavfile import write
def record():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file 

def playnote(a):
    mixer.init()
    if a=='c':
        mixer.music.load('piano_middle_C.mp3')
        mixer.music.play()
    elif a=='c#':
        mixer.music.load('piano_C_sharp.mp3')
        mixer.music.play()
    elif a=='d':
        mixer.music.load('piano_D.mp3')
        mixer.music.play()
    elif a=='d#':
        mixer.music.load('piano_D_sharp.mp3')
        mixer.music.play()
    elif a =='e':
        mixer.music.load('piano_E.mp3')
        mixer.music.play()
    elif a == 'f':
        mixer.music.load('piano_F.mp3')
        mixer.music.play()
    elif a == 'f#':
        mixer.music.load('piano_F_sharp.mp3')
        mixer.music.play()
    elif a == 'g':
        mixer.music.load('piano_G.mp3')
        mixer.music.play()
    elif a == 'g#':
        mixer.music.load('piano_G_sharp.mp3')
        mixer.music.play()
    elif a == 'a':
        mixer.music.load('piano_A.mp3')
        mixer.music.play()
    elif a == 'a#':
        mixer.music.load('piano_A_sharp.mp3')
        mixer.music.play()
    elif a == 'b':
        mixer.music.load('piano_B.mp3')
        mixer.music.play()
       


root = tkinter.Tk()
root.geometry("1000x500")
cbtn = tkinter.Button(root, bg = "white",text = 'C', width = 10,height = 10 , command =lambda:playnote('c'))
csbtn = tkinter.Button(root, bg = "black", text = '', width = 10,height = 10 , command =lambda:playnote('c#'))
dbtn = tkinter.Button(root,bg = "white", text = 'D', width = 10,height = 10 , command = lambda:playnote('d'))
dsbtn = tkinter.Button(root, bg = "black",text = '', width = 10,height = 10 , command = lambda:playnote('d#'))
ebtn = tkinter.Button(root,bg = "white", text = 'E', width = 10,height = 10 , command = lambda:playnote('e'))
fbtn = tkinter.Button(root,bg = "white", text = 'F', width = 10,height = 10 , command = lambda:playnote('f'))
fsbtn = tkinter.Button(root,bg = "black", text = '', width = 10,height = 10 , command = lambda:playnote('f#'))
gbtn = tkinter.Button(root, bg = "white",text = 'G', width = 10,height = 10 , command = lambda:playnote('g'))
gsbtn = tkinter.Button(root, bg = "black",text = '', width = 10,height = 10 , command = lambda:playnote('g#'))
abtn = tkinter.Button(root, bg = "white",text = 'A', width = 10,height = 10 , command =lambda:playnote('a'))
asbtn = tkinter.Button(root, bg = "black",text = '', width = 10,height = 10 , command =lambda:playnote('a#'))
bbtn = tkinter.Button(root,bg = "white", text = 'B', width = 10,height = 10 , command = lambda:playnote('b'))
record_btn = tkinter.Button(root, text = 'record',command = record())

cbtn.grid(column= 0, row=1)
csbtn.grid(column= 1, row=0)
dbtn.grid(column= 2, row=1)
dsbtn.grid(column= 3, row=0)
ebtn.grid(column= 4, row=1)
fbtn.grid(column= 5, row=1)
fsbtn.grid(column= 6, row=0)
gbtn.grid(column= 7, row=1)
gsbtn.grid(column= 8, row=0)
abtn.grid(column= 9, row=1)
asbtn.grid(column= 10, row=0)
bbtn.grid(column= 11, row=1)
record_btn.grid(column =6, row= 2)

#cbtn.pack(side = tkinter.LEFT)
#csbtn.pack(side = tkinter.LEFT)
#dbtn.pack(side = tkinter.LEFT)
#dsbtn.pack(side = tkinter.LEFT)
#ebtn.pack(side = tkinter.LEFT)
#fbtn.pack(side = tkinter.LEFT)
#fsbtn.pack(side = tkinter.LEFT)
#gbtn.pack(side = tkinter.LEFT)
#gsbtn.pack(side = tkinter.LEFT)
#abtn.pack(side = tkinter.LEFT)
#asbtn.pack(side = tkinter.LEFT)
#bbtn.pack(side = tkinter.LEFT)
root.mainloop()
