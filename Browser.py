import subprocess
import pip
try:
	import webbrowser
except:
    pip.main(["install","webbrowser"])
    import webbrowser
    
def browse(link):
    webbrowser.open_new_tab(link)

#browse("https://docs.python.org/2/library/webbrowser.html")