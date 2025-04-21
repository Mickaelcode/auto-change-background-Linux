import os 
import argparse
import time 
from random import choice 

parser = argparse.ArgumentParser()
parser.add_argument('-P','--path',help="directory background's all path", required=True)
parser.add_argument('-T','--time',type=float,help="time in seconde that you need to change your background")
args = parser.parse_args()
path = args.path 
time_arg = args.time 
times = time_arg if time_arg else 20.0

data = os.listdir(path)

wallpapers = list(map(lambda n : f"file://{path}/{n}",data))

while True:
    wallpaper = choice(wallpapers)
    os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {wallpaper}')
    time.sleep(times)

