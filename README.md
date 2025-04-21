# How to install
- clone the repo or download the zip

# Requirement
- Make sure that you have been installed python(3.*) and these module:
  - os
  - argparse
  - time
  - random

# How to use it
- You need to create a directory that have your all pictures background (eg : in `/home/user_name/Pictures`)
- Run the command `python3 wallpaper.py -P<path> -T<time>`
  - the `-P` : path to your pictures directory ; eg: if in `Pictures/` from `home/` that must be => ` python3 wallpaper.py -P /home/user_name/Pictures` 
  - the `-T` : this is the time(seconds) that you need to change randomly your background ; eg:for 10 seconds  in `Pictures/` 's pictures => ` python3 wallpaper.py -P /home/user_name/Pictures -T 10`
      - It is no required argument but  by default it's 20 seconds ; eg =>` python3 wallpaper.py -P /home/user_name/Pictures`

# Set Up Autostart (Optional but recommended)
- Open "Startup Applications" (via system settings or by running `gnome-session-properties` in a terminal).

- Click "Add" and fill in the details:
  - Name: Wallpaper Changer
  - Command: `python3 /path/to/the/wallpaper.py -P "/path/to/your/wallpapers_directory" -T<time>`
  - Comment: Changes wallpaper periodically
