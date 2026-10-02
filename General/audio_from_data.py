
from gtts import gTTS
import os
from tkinter import *


'''text = "Hoy es un excelente dia para comenzar con todo lo que te propongas."     ##TEXTO

output = gTTS(text=text, lang = 'es', slow=False)
output.save('output.mp3')                                                       ###ESTE CODIGO CONVIERTE TEXTO EN AUDIO

os.system("start output.mp3")                        ##ESTE ES PARA REPRODUCIRLO    '''                            





'''---------------------------------------------------------------------------------------------------------------------------------------------
text = open('file_audio.txt','r').read()                                ###GENERA UN AUDIO DE UN TEXTO QUE ESTE EN UN ARCHVIO .TXT

language ='es'
(file_audio.txtoutput = gTTS(text=text,lang=language,tld='com.mx',slow=False)               ## EL ARCVHIVO ES file_audio.txt

output.save('fileoutput.mp3')
os.system("start fileoutput.mp3")

------------------------------------------------------------------------------------------------------------------------------------------------
'''

def textToSpeech():
    text=entry.get()
    language='en'
    output = gTTS(text=text,lang=language,slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")



root =Tk()

canvas = Canvas(root,width=400,height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text="Start",command=textToSpeech)
canvas.create_window(200,230,window=button)

root =mainloop()


