# For importing modules
import Names
import Downloader
import Browser
import Wikia

# For GUI
import tkinter as tk
#from tkinter import *
#from tkinter import ttk
#import Browser

# Function
def control(event = None):      # use "event = None" when error occurs
    mesg = myMesg.get()
    mesgList.insert(tk.END,Names.getNames("master")+": "+mesg)
    myMesg.set("")
    #print(mesg)
    mesg = mesg.split(" ")
    command = mesg[0]
    if command.lower() == "download":
        Downloader.Download(mesg[1])
    elif command.lower() == "search" or command.lower() == "browse":
        Browser.browse(mesg[1])
    elif command.lower() == "wikia":
        if len(mesg) == 2:
            wikia.wiki(mesg[1],mesg[1])
        elif len(mesg) == 3:
            Wikia.wiki(mesg[1],mesg[2])
        


root = tk.Tk()
root.title("Caliban")
root.iconbitmap("Caliban.ico")
root.bind("<Return>",control)

messageFrame = tk.Frame(root)
myMesg = tk.StringVar()
myMesg.set(Names.getNames("command"))
scrollbar = tk.Scrollbar(messageFrame)

# To contain the mesage
mesgList = tk.Listbox(messageFrame,height = 20, width = 70, yscrollcommand = scrollbar.set)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
mesgList.pack(side = tk.LEFT, fill = tk.BOTH)
mesgList.pack()
messageFrame.pack()

#entryField = tk.Entry(bottom, textvariable = myMesg)
entryField = tk.Entry(root, textvariable = myMesg)
#entryField.bind("<Enter>",control)
entryField.pack()
#sendButton = tk.Button(bottom, text = "Send",command = )
sendButton = tk.Button(root, text = "Enter",command = control)
sendButton.pack()



root.mainloop()