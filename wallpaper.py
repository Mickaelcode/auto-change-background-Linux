import os 
import argparse
import time 

parser = argparse.ArgumentParser()
parser.add_argument('-P','--path',help="directory background's path")

args = parser.parse_args()
if not args:
    os.system('echo argument required')
    os.system('python3 wallpaper.py --help')
    exit

data = os.listdir(os.path.expanduser(f'~/{args.path}'))

wallpapers = list(map(lambda n : f"file:///home/mickael/Pictures/{n}",data))


i = 0 

while i<len(wallpapers):
    os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {wallpapers[i]}')
    i+=1
    if i==len(wallpapers):i=0
    time.sleep(20.0)


