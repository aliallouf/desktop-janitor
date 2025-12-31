import os
import shutil
import schedule
import time
def folder_janitor():
    target_dir = "" 
    extensions_map = {
        ".pdf": "Documents",
        ".jpg": "Images",
        ".png": "Images",
        ".zip": "Archives"
    }
    
    os.chdir(target_dir)
    for filename in os.listdir(target_dir):
        name, extension = os.path.splitext(filename)
        if extension in extensions_map:
            dest = extensions_map[extension]
            if not os.path.exists(dest):
                os.makedirs(dest)
            shutil.move(filename, dest)
    print("Cleanup Complete!")

# 1. Schedule the task (24-hour format)
schedule.every().day.at("18:00").do(folder_janitor)
print("Janitor is standing by... do not close the window.")
# 2. keep the script runing
while True:
    schedule.run_pending()
    time.sleep(60) # Wait 60 seconds before checking the clock again