# For importing modules
import Names
import Downloader
import Browser
import Wikia
import WebAutomation

# For GUI
import tkinter as tk
#from tkinter import *
#from tkinter import ttk
#import Browser

# Global Variables
content = ""
email = ""
password = ""

# Function
def youTube(event = None):
    print(content.get())
    WebAutomation.openYoutube(content.get())

def Facebook(event = None):
    WebAutomation.openFacebook(email.get(),password.get())

def control(event = None):      # use "event = None" when error occurs
    mesg = myMesg.get()
    if mesg != "":
        mesgList.insert(tk.END,Names.getNames("master")+": "+mesg)
    myMesg.set("")
    #print(mesg)
    mesg = mesg.split(" ")
    command = mesg[0]
    if command.lower() == "download":
        mesgList.insert(tk.END,"Caliban : Starting Download")
        Downloader.Download(mesg[1])
    elif command.lower() == "search" or command.lower() == "browse":
        mesgList.insert(tk.END,"Caliban : Comencing Search...")
        mesgList.insert(tk.END,"Caliban : Launching Browser")
        Browser.browse(mesg[1])
    elif command.lower() == "wikia":
        mesgList.insert(tk.END,"Caliban : Loading Wikia in Default Browser")
        if len(mesg) == 2:
            Wikia.wiki(mesg[1],mesg[1])
        elif len(mesg) == 3:
            Wikia.wiki(mesg[1],mesg[2])
    elif command.lower() == "open":
        if mesg[1].lower() == 'youtube':
            global content
            youtube = tk.Tk()
            youtube.title("youTube")
            youtube.iconbitmap("Caliban.ico")
            youtube.bind("<Return>",youTube)
            name = tk.Label(youtube, text = "Enter the search content")
            name.pack()
            content = tk.Entry(youtube)
            content.pack()
            youtube.mainloop()
        elif mesg[1].lower() == 'facebook':
            global email, password
            facebook = tk.Tk()
            facebook.title("Facebook")
            facebook.iconbitmap("Caliban.ico")
            facebook.bind("<Return>",Facebook)
            mail = tk.Label(facebook, text = "Enter the email Id")
            mail.pack()
            email = tk.Entry(facebook)
            email.pack()
            paswd = tk.Label(facebook, text = "Enter the password")
            paswd.pack()
            password = tk.Entry(facebook)
            password.pack()
            facebook.mainloop()
            

    mesgList.insert(tk.END,"Caliban : Task Completed")
        


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