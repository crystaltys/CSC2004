#Python GUI
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import Canvas, Scrollbar
from tkinter import filedialog
from PIL import ImageTk,Image  
from bpcs import BPCS
from message import Message
from cv2 import cv2

class GUI:

    def __init__(self, window):
        
        # parent window 
        self.window = window
        self.window.title("QuickStego")
        self.window.geometry("810x450")
        self.window.resizable(0, 0)
        
        # child window
        self.child = ttk.Notebook(self.window) 
        
        # menu bar
        self.encodeTab = ttk.Frame(self.child) 
        self.decodeTab = ttk.Frame(self.child) 
        self.child.add(self.encodeTab, text ="Encoding") 
        self.child.add(self.decodeTab, text ="Decoding") 
        self.child.grid(row=0,column=0,pady=2,padx=2,columnspan=7,rowspan=7,sticky=tk.W)
        
        # widgets
        self.titleBar(self.encodeTab,self.decodeTab) 
        self.btn(self.encodeTab,self.decodeTab) 
        self.entryBox(self.encodeTab,self.decodeTab)
        
        # img widgets 
        self.inputImage = tk.Canvas(self.encodeTab,width=260,height=300,background="white")
        self.inputImage.grid(row=2,column=0,columnspan=2,rowspan=3,padx=2,sticky=tk.NW)
        self.outputImage = tk.Canvas(self.encodeTab,width=260,height=300,background="white")
        self.outputImage.grid(row=2,column=5,columnspan=2,rowspan=3,padx=2,sticky=tk.NW)   
    
    def titleBar(self,encode,decode):
        # left pane 
        self.orgimgLabel = ttk.Label(encode,text="Cover Image")
        self.orgimgLabel.grid(row=1,column=0,pady=5,padx=2,sticky=tk.SW)
        # middle pane
        self.secretMsg = ttk.Label(encode,text="Secret Payload")
        self.secretMsg.grid(row=1,column=2,columnspan=3,pady=5,padx=10,sticky=tk.W)
        self.secretKey = ttk.Label(encode,text="Secret Key")
        self.secretKey.grid(row=4,column=2,columnspan=1,pady=5,padx=4,sticky=tk.W)
        self.threshold = ttk.Label(encode,text="Threshold")
        self.threshold.grid(row=5,column=2,columnspan=1,pady=5,padx=4,sticky=tk.W)
        # right pane
        self.stegoimgLabel = ttk.Label(encode,text="Stego Image")
        self.stegoimgLabel.grid(row=1,column=5,pady=5,sticky=tk.W)

    def btn(self,encode,decode):  
        # left pane   
        self.uploadButton=ttk.Button(encode,text="Browse",padding=2,command=self.load_coverImg)
        self.uploadButton.grid(row=5,column=0,padx=2,pady=5,ipady=4,ipadx=26,sticky=tk.NW)
        self.resetButton=ttk.Button(encode,text="Clear",padding=2,command=self.clear_coverImg)
        self.resetButton.grid(row=5,column=1,padx=2,pady=5,ipady=4,ipadx=26,sticky=tk.NW)
        self.createButton=ttk.Button(encode,text="Start Encoding",padding=2)
        self.createButton.grid(row=5,column=5,columnspan=2,padx=2,pady=4,ipady=4,ipadx=85,sticky=tk.NW)
        self.createButton.bind("<Button-1>", self.encode)
    
    def entryBox(self,encode,decode):  
        # middle pane
        self.secretMsg_txtBox = tk.Text(encode, height=16, width=30)
        self.secretMsg_txtBox.grid(row=2,column=2,columnspan=3,rowspan=2,padx=8,sticky=tk.W) 
        self.secretMsg_txtBox.bind("<Leave>", self.getSecretPayload)
        self.txtsecretKey=StringVar()
        self.entryKey=ttk.Entry(encode,textvariable=self.txtsecretKey,width=28)
        self.entryKey.grid(row=4,column=3,pady=5,ipady=4,sticky=tk.NSEW)   
        self.entryKey.bind("<Leave>", self.getSecretKey)
        
        self.txtThreshold=StringVar()
        self.txtThreshold.set("0.3")
        self.entryThreshold=ttk.Entry(encode,textvariable=self.txtThreshold,width=28)
        self.entryThreshold.grid(row=5,column=3,pady=5,ipady=5,sticky=tk.NSEW)   

    # event functions
    
    def load_coverImg(self):
        self.filename = filedialog.askopenfilename(initialdir="./img", title="Open File", filetype =(("*.png","*.png"),("*.jpg","*.jpg"),("*.bmp","*.bmp"),("All Files","*.*")))
        # create PIL image
        self.img = Image.open(self.filename)
        self.img.thumbnail((300, 400), Image.ANTIALIAS)
        #create photoimage
        self.image = ImageTk.PhotoImage(self.img)
        self.inputImage.create_image(0,0,image=self.image, anchor=tk.NW)
       
    def clear_coverImg(self):
        self.inputImage.delete("all")
    
    def getSecretPayload(self,event): # secret message
        msgInput = self.secretMsg_txtBox.get("1.0","end-1c")
        if len(self.secretMsg_txtBox.get("1.0","end-1c")) == 0 or '':
            return(None)
        else: 
            # Added to check payload
            print("Payload: ", msgInput)
            return(msgInput)
  
    
    def getSecretKey(self,event):
        self.keyInput = self.txtsecretKey.get()
        if len(self.keyInput) == 0 or '':
            return(None)
        else: 
            # Added to check secret key
            print("Key: ", self.keyInput)
            return(self.keyInput)
   
    def getThreshold(self,event):
        threshold = self.txtThreshold.get()
        if len(threshold) == 0:
            return(None)
        else: 
            return(threshold)

    def load_stegoImg(self):
        self.steg_img = Image.open('saved.png')
        self.steg_img.thumbnail((300, 400), Image.ANTIALIAS)
        #create photoimage
        self.steg_image = ImageTk.PhotoImage(self.steg_img)
        self.outputImage.create_image(0,0,image=self.steg_image, anchor=tk.NW)

    def encode(self,event):
        bpcs = BPCS(self.filename) 
        orig_extension = self.filename.split('.')[-1]
        encrypted = True if self.getSecretKey(event)!= None else False
        message = True if self.getSecretPayload(event)!= None else False
        threshold = 0.3
        if (message is False):
            tk.messagebox.showerror(title="Error", message="Enter Secret Payload")
        else:
            # original
            # msg = Message(message=self.getSecretPayload(event), encrypted = encrypted, key = self.getSecretKey(event), threshold = threshold)
            
            # Zy's code
            msg = Message(pathname=self.filename, encrypted=encrypted, key=self.getSecretKey(event), threshold=threshold)
            print('Loading Please wait...')
            bitplane_msg = msg.create_message()
            img_result = bpcs.hide(bitplane_msg, randomize=True, key=self.getSecretKey(event), threshold = threshold)
            cv2.imwrite('saved.png', img_result)

            # create photoimage
            img_result = ImageTk.PhotoImage(self.img)
            self.load_stegoImg()
            print('Finished encoding!')

if __name__ == "__main__":
    window = tk.Tk()
    GUI(window)
    window.mainloop()
