import tkinter
import requests




#def Window()
root = tkinter.Tk()
tkinter.Label(root,text = "URL").grid(row = 0)
tkinter.Label(root,text = "Name of the File").grid(row = 1)
url = tkinter.Entry(root)
name = tkinter.Entry(root)

url.grid(row = 0, column = 1)
name.grid(row = 1, column = 1)

def Download():
#    global urlD
#    global nameD
    global root
    urlD = url.get()
#    print(urlD)
    nameD = name.get()
    r = requests.get(urlD,stream = True)                #, allow_redirection = True
    with open(nameD,"wb") as down:
        for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
                down.write(chunk)
    root.quit()

tkinter.Button(root,text = "Download",command =Download).grid(row=3)

tkinter.mainloop()
#Window()