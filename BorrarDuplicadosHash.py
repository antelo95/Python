
from tkinter.filedialog import askdirectory
  
# Importing required libraries.
from tkinter import Tk
import os
import hashlib
from pathlib import Path
from humanize import naturalsize

Tk().withdraw()
  
file_path = askdirectory(title="Select a folder")

list_of_files = os.walk(file_path)
  
# In order to detect the duplicate
# files we are going to define an empty dictionary.
unique_files = dict()
deletedSize = 0 
for root, folders, files in list_of_files:  
    for file in files:
  
        file_path = Path(os.path.join(root, file))
        Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
  
        if Hash_file not in unique_files:
            unique_files[Hash_file] = file_path
        else:
            size = os.stat(file_path).st_size
            deletedSize += size
            os.remove(file_path)
            print(f"{file_path} has been deleted")
print(f"{naturalsize(deletedSize)} total")