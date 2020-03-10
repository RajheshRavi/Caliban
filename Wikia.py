import subprocess
import Browser
import pip
#import sys

try:
    import wikia
except:
	#subprocess.check_call([sys.executable,"-m",pip,"install","wikia"])
    pip.main(['install','wikia'])
    import wikia

def wiki(topic,subtopic):
    wiki = wikia.page(topic,subtopic)
    Browser.browse(wiki.url)

#wiki("huntik","huntik")
#wiki("huntik","caliban")