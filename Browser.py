import subprocess

try:
	import webbrowser
except:
	subprocess.check_call([sys.executable,"-m",pip,"install","webbrowser"])
    #import webbrowser

def browse(link):
    webbrowser.open_new_tab(link)

#browse("https://docs.python.org/2/library/webbrowser.html")