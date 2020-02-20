import subprocess
import browser

try:
    import wikia
except:
	subprocess.check_call([sys.executable,"-m",pip,"install","wikia"])

def wiki(topic,subtopic):
    wiki = wikia.page(topic,subtopic)
    browser.browse(wiki.url)

#wiki("huntik","caliban")