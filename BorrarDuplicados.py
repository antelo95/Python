from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
from pathlib import Path
from humanize import naturalsize

Tk().withdraw()
path = askdirectory(title="Seleccionar directorio")
directoryList = os.walk(path)
deletedSize = 0

for root, foldes, files in directoryList:
    for file in files:    
        #print(file)
        if ")." in file:
            filePath = Path(os.path.join(root, file))
            size = os.stat(filePath).st_size
            deletedSize += size
            print(f"El archivo {filePath} Ha sido borrado {naturalsize(size)}")
            os.remove(filePath)
print(f"Total borrado: {naturalsize(deletedSize)}")