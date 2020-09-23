#Python GUI
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import Canvas
from tkinter import filedialog
from PIL import ImageTk,Image  

global img

class GUI():
    def __init__(self, window):

        # basic windows frame 
        self.window = window
        self.window.title("SteganographyGUI")
        self.tabControl = ttk.Notebook(self.window) 
        self.window.geometry("810x450")
        self.window.resizable(0, 0)
        
        # top bar tab
        self.encodeTab = ttk.Frame(self.tabControl) 
        self.decodeTab = ttk.Frame(self.tabControl) 
        self.tabControl.add(self.encodeTab, text ="Encoding") 
        self.tabControl.add(self.decodeTab, text ="Decoding") 
        self.tabControl.grid(row=0,column=0,pady=2,padx=2,columnspan=3,rowspan=7,sticky=tk.W)

        # left pane 
        self.orgimgLabel = ttk.Label(self.encodeTab,text="Original Image")
        self.orgimgLabel.grid(row=1,column=0,pady=5,padx=2,sticky=tk.SW)
        self.inputImage = Canvas(self.encodeTab,width=260,height=260,background="white")
        self.inputImage.grid(row=2,column=0,columnspan=2,rowspan=5,padx=2,sticky=tk.NW)
        self.uploadButton=ttk.Button(self.encodeTab,text="Browse",padding=2,command=self.load_coverimg)
        self.uploadButton.grid(row=4,column=0,padx=2,ipady=4,ipadx=25,sticky=tk.NW)
        self.resetButton=ttk.Button(self.encodeTab,text="Clear",padding=2)
        self.resetButton.grid(row=4,column=1,padx=2,ipady=4,ipadx=25,sticky=tk.NW)

        # middle pane
        self.keyLabel = ttk.Label(self.encodeTab,text="Encryption Key")
        self.keyLabel.grid(row=1,column=2,columnspan=3,pady=5,padx=10,sticky=tk.W)
        self.txtEncryptionKey=StringVar()
        self.entryKey=ttk.Entry(self.encodeTab,textvariable=self.txtEncryptionKey,width=40)
        self.entryKey.grid(row=2,column=2,columnspan=3,padx=10,pady=2,ipady=120,sticky=tk.NW)   
        self.secretmsgLabel = ttk.Label(self.encodeTab,text="Secret Message")
        self.secretmsgLabel.grid(row=3,column=2,padx=10,pady=2,sticky=tk.NW)
        self.txtSecretMsg=StringVar()
        self.secretMsg=ttk.Entry(self.encodeTab,textvariable=self.txtSecretMsg,width=40)
        self.secretMsg.grid(row=4,column=2,columnspan=3,padx=10,ipady=5,sticky=tk.NW)
        self.thresholdLabel = ttk.Label(self.encodeTab,text="Threshold")
        self.thresholdLabel.grid(row=5,column=2,padx=10,sticky=tk.NW)
        self.txtThreshold=StringVar()
        self.threshold=ttk.Entry(self.encodeTab,textvariable=self.txtThreshold,width=40)
        self.threshold.grid(row=6,column=2,columnspan=3,padx=10,sticky=tk.NW)

        # right pane
        self.stegoimgLabel = ttk.Label(self.encodeTab,text="Stego Image")
        self.stegoimgLabel.grid(row=1,column=5,pady=5,padx=2,sticky=tk.SW)
        self.outputImage = tk.Canvas(self.encodeTab,width=260,height=260,background="white")
        self.outputImage.grid(row=2,column=5,columnspan=2,rowspan=2,padx=2,sticky=tk.NW)

        self.createButton=ttk.Button(self.encodeTab,text="Create Stego Image",padding=2,command=self.load_coverimg)
        self.createButton.grid(row=4,column=5,columnspan=2,padx=2,ipady=4,ipadx=75,sticky=tk.NW)
    
    def load_coverimg(self):
        self.filename = filedialog.askopenfilename(initialdir="./", title="Select An Image", filetype =(("png","*.png"), ("All Files","*.*")))
        self.inputImage.create_image(120, 60,image=img) 
    
    #def encrypt(self):


if __name__ == "__main__":
    window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("test.png"))  
    GUI(window)
    window.mainloop()
