from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
from pathlib import Path
from humanize import naturalsize

Tk().withdraw()
path = askdirectory(title="Seleccionar directorio")
directoryList = os.walk(path)
deletedSize = 0
for root, folders, files in directoryList:
    for file in files:
        file_path = Path(os.path.join(root, file))
        size = os.stat(file_path).st_size
        deletedSize += size
print(f"El directorio: {path} tiene {naturalsize(deletedSize)}")