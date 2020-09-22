#Python GUI
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("SteganographyGUI")
window.geometry("600x600")
window.resizable(0, 0)

labelframe = ttk.LabelFrame(window,text="Encoding",borderwidth=1)
labelframe.grid(columnspan=8,rowspan=10,padx=20,pady=10)

insertButton=ttk.Button(labelframe,text="Load Image",padding=2) #need to write command = ""
insertButton.grid(row=1,column=0,columnspan=2,pady=10,padx=15,sticky=tk.W)

figure = Figure(figsize=(4, 3), dpi=100, facecolor="#F0F0F0")
plot = figure.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(figure, labelframe)
canvas.get_tk_widget().grid(row=0, column=2,columnspan=6,rowspan=3,pady=20,padx=20,sticky=tk.E)

msgButton=ttk.Button(labelframe,text="Enter your Message",padding=2,width=70) #need to write command = ""
msgButton.grid(row=4,columnspan=8,pady=3,padx=15,sticky=tk.EW)

msglengthButton=ttk.Button(labelframe,text="Enter layer to set msg length",padding=2,width=70) #need to write command = ""
msglengthButton.grid(row=5,columnspan=8,pady=3,padx=15,sticky=tk.EW)

encodingButton=ttk.Button(labelframe,text="Enter layer to set msg encoding",padding=2,width=70) #need to write command = ""
encodingButton.grid(row=6,columnspan=8,pady=3,padx=15,sticky=tk.EW)

rgblayerButton=ttk.Button(labelframe,text="Enter layer to set password",padding=2,width=70) #need to write command = ""
rgblayerButton.grid(row=7,columnspan=8,pady=3,padx=15,sticky=tk.EW)

pwsdButton=ttk.Button(labelframe,text="Enter Password between 0-255",padding=2,width=70) #need to write command = ""
pwsdButton.grid(row=8,columnspan=8,pady=3,padx=15,sticky=tk.EW)

pwsdButton=ttk.Button(labelframe,text="Encode",padding=2) #need to write command = ""
pwsdButton.grid(row=9,column=4,pady=20,padx=15,sticky=tk.W)



window.mainloop() #main loop to wait for events
