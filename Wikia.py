import subprocess
import browser
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
    browser.browse(wiki.url)

#wiki("huntik","caliban")