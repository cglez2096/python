
import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog

def compression (i,o):
    compress(i,o)

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title = "Select a file to descompress")
    return filename


window = tk.Tk()
window.title("COMPRESSION ENGINE")
window.geometry("350x350")



'''input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text="File to be compresses")
output_label = tk.Label(window,text="Name of the compressed file")'''

compress_button = tk.Button(window,text="Compress",command=lambda:compression(open_file(),"output1.txt"))

'''input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)

output_label.grid(row=1,column=0)
output_entry.grid(row=1,column=1)'''

compress_button.grid(row=2,column=1)







window.mainloop()

