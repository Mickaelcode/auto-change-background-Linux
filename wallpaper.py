import os 
import time 


data = os.listdir('./Pictures')

wallpapers = list(map(lambda n : f"file:///home/mickael/Pictures/{n}",data))


i = 0 

while i<len(wallpapers):
    os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {wallpapers[i]}')
    i+=1
    if i==len(wallpapers):i=0
    print(i)
    time.sleep(5.0)


