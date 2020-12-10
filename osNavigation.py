import os
import shutil

for folderName, subfolders, fileNames in os.walk('[ABSOLUTE_PATH]'):
    print('The folder is ' + folderName)
    print('The subfolder in ' + folderName + ' are: ' + str(subfolders))
    print('The file name/s in ' + folderName + ' are: ' + str(fileNames))
    print()

    for sf in subfolders:
        if 'dog' in subfolders:
            os.rmdir(sf)

    for file in fileNames:
        if file.endsWith('.py'):
            shutil.copy(os.join(folderName, file), \
                    os.join(folderName, file + '.backup'))