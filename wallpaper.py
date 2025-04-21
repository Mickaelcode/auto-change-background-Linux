import os 
import argparse
import time 
import sys 
from random import choice 

parser = argparse.ArgumentParser()
parser.add_argument('-P','--path',help="directory background's all path")
args = parser.parse_args()
path = args.path 

if not path:
    os.system('echo argument required')
    os.system('python3 wallpaper.py --help')
    sys.exit()

data = os.listdir(path)

wallpapers = list(map(lambda n : f"file://{path}/{n}",data))

while True:
    wallpaper = choice(wallpapers)
    os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {wallpaper}')
    print(wallpaper)
    time.sleep(20.0)


