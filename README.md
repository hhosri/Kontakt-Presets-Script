# Kontakt-Presets

## Description

Kontakt-Presets is a Python script that moves the Kontakt presets to the correct default folder. It is especially useful for independent small Kontakt developers who are releasing non-licensed Kontakt instruments and want the user to be able to use snapshots (presets) without the hassle of copying anything.

The script is designed to work seamlessly, and if done properly by the developer, the user would only have to run (double-click) the executable and that's it! Without the need to have python installed on their computer or even the need of opening the terminal.

## Developer Instructions

### Pre-requisites
- Kontakt instrument with snapshots saved as .nksn files
- Python and Pyinstaller installed on your machine

### Steps
1. Open your Kontakt instrument, and start creating, naming and saving snapshots (Camera icon, on the upper box). When you create your first snapshot, Kontakt will automatically create a folder with the same name as your instrument (the .nki file).
   - MAC: `/Users/username/Documents/Native Instruments/User Content/Kontakt`
   - WINDOWS: `C:\Users\username\My Documents\Native Instruments\User Content\Kontakt`

   Every time you save a new snapshot, it will be saved inside this folder as a .nksn file.

2. After creating the snapshots, create (in your Kontakt instrument folder) a folder named "Presets" (can be any name).

3. Copy the folder with the .nksn files into the "Presets" folder that you just created. (Make sure NOT to change the name of the .nksn folder that you just copied, as it should always have the same name as the .nki file)

4. After moving the folder with the .nksn files into your "Presets" folder, copy the KontaktPresets.py script also to the "Presets" folder. (Both the folder with the snapshots and the python script should be in the same "Presets" folder).

5. Open the KontaktPresets.py script and assign to the variable `instrumentName` the actual name of your instrument. e.g.: `instrumentName = "MyPiano"`

6. Save and close.

7. Open a terminal and cd to the "Presets" folder.

8. Run the following command:
```
python3 -m PyInstaller --add-data FolderName:FolderName --onefile KontaktPresets.py
```
   Replace `FolderName` (both after and before the :) with the actual name of the instrument or the name of the folder that contains the snapshots (both should have the same name).

9. Some folders are going to be generated, go to the folder "dist," and there you can find the executable named KontaktPresets. Copy it to the "Presets" folder.

10. Now you can delete everything that was generated by the script, and ONLY KEEP 2 files in the "Presets" folder:
   1. The folder with the .nksn files
   2. The executable that you've just copied (You can delete the KontaktPresets.py script now)

## User Instructions

After downloading the instrument, the user can go to the "Presets" folder and double-click the executable KontaktPresets. That's it!
