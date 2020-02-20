import subprocess
try:
    import vlc
except:
    subprocess.check_call([sys.executable,"-m",pip,"install","vlc"])
    import vlc


def play(location):
    mediaPlayer = vlc.MediaPlayer(location)
    mediaPlayer.play()