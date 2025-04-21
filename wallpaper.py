import os 
import argparse
import time 
import sys 

parser = argparse.ArgumentParser()
parser.add_argument('-P','--path',help="directory background's path")

args = parser.parse_args()
if not args.path:
    os.system('echo argument required')
    os.system('python3 wallpaper.py --help')
    sys.exit()    
print(os.path.abspath(args.path))
wallpapers_path = f'~/{args.path}'
data = os.listdir(os.path.expanduser(wallpapers_path))

wallpapers = list(map(lambda n : f"file://{wallpapers_path}/{n}",data))


i = 0 

while i<len(wallpapers):
    os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {wallpapers[i]}')
    print(wallpapers[i])
    i+=1
    if i==len(wallpapers):i=0
    time.sleep(20.0)


