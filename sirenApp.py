import librosa
import librosa.display
from tkinter import *
from pygame import mixer
import IPython as ipd
import pandas as pd
import numpy as np
import os
import tkinter .font as font
from tkinter import filedialog
import time
from tensorflow.keras.models import load_model
import pathlib
dirPath = pathlib.Path(__file__).parent.resolve()
print(str(dirPath))
m1 = load_model(os.path.join(dirPath,'test4.h5'))

arr=["24631-6-0-0.wav","21683-9-0-18.wav","57323-8-0-0.wav","57323-8-0-6.wav","81788-2-0-51.wav"]


# Feature extraction with librosa


def features_extract(file):
    audio,sample_rate=librosa.load(file,res_type='kaiser_fast')
    mfccs_features=librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc=40) 
    mfccs_scaled=np.mean(mfccs_features.T,axis=0)
    
    return mfccs_scaled


#precition of the sound by trained model

def cls(file):
    pf = features_extract(file)
    pf = pf.reshape(1,-1)
    t = m1.predict(pf)
    simp= t[0]
    gtr = 0
    for i in range(len(simp)):
        if simp[i] > simp[gtr]:
            gtr = i
    return gtr


def prediction():
    out.delete("1.0","end")
    song=songs_list.get(ACTIVE)
    song= str(dirPath)+"/sounds/" + song
    res=cls(song)
    t='not a siren'
    if res==8:
        t="siren"
    out.insert(END,t)


def play():
    song=songs_list.get(ACTIVE)
    song=str(dirPath)+"/sounds/" + song
    mixer.music.load(song)
    mixer.music.play(loops=1)
    time.sleep(1)
    prediction()

def add():
    for i in arr:
        songs_list.insert(END,i)



root=Tk()
mixer.init()
root.geometry('300x300')
songs_list=Listbox(root,bg='black',fg='white',height=10,width=15)
add_bt=Button(root,text="add",bd='5',command=add)
nxt=Button(root,text="play",bd='5',command=play)
out=Text(root,height=1,width=15)
#test.pack(side='left')
#play_all=Button(root,text="play all",bd='5',command=ply)
songs_list.grid(row=1,column=2)
out.grid(row=3,column=2)
add_bt.grid(row=4,column=1)
nxt.grid(row=4,column=4)
#play_all.grid(row=1,column=2)
root.mainloop()