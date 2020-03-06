import tkinter
import requests



def Download(urlD):
    r = requests.get(urlD,stream = True, allow_redirection = True)                #, allow_redirection = True
    with open(urlD.split('/')[-1],"wb") as down:
        for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
                down.write(chunk)