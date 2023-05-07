import os
import shutil
import getpass
import platform
import sys

# user
username = getpass.getuser()

# destination dir
if platform.system() == 'Darwin':
    dest_dir = "/Users/" + username + "/Documents/Native Instruments/User Content/Kontakt"
elif platform.system() == 'Windows':
    dest_dir = "C:\\Users\\" + username + "\\My Documents\\Native Instruments\\User Content\\Kontakt"
else:
    print("\033[91mError: This script does not support your system\033[0m")
    sys.exit()

# InstrumentName (CHANGE THIS)
instrumentName = #presets_folder_name

# current script dir
# checks if we are running the program with a script or with an executable, and gets the appropriate path
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

# presets source dir
presets_dir_src = os.path.join(current_dir, instrumentName)

# destination preset dir (check if it already exists)
dest_preset_dir = os.path.join(dest_dir, instrumentName)

if not os.path.exists(presets_dir_src):
    print(f"\033[91mError: '{instrumentName}' folder not found in the same directory as the script.\033[0m")
    sys.exit()

if not os.path.exists(dest_dir):
    print(f"\033[91mError: Destination directory '{dest_dir}' does not exist. Make sure Kontakt 6 is installed on your machine\033[0m")
    sys.exit()

if os.path.exists(dest_preset_dir):
    for file_name in os.listdir(presets_dir_src):
        src_path = os.path.join(presets_dir_src, file_name)
        dst_path = os.path.join(dest_preset_dir, file_name)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
else:
    shutil.copytree(presets_dir_src, dest_preset_dir)
print("\033[32mPresets copied succesfully!\033[0m")
sys.exit()
