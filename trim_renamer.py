import os
import sys

# path = the full path to a directory that contains files to rename
# appendText = text to append at start
# appendTextIncrement = For every file, increment a number and add it to the end of the text
# appendTextDivider = Add a divider between trimmed/appended content and the rest of the filename
# trimAmount = words to be trimmed at start

path = r""
appendText = r""
appendTextIncrement = True
appendTextDivider = r" - "
trimAmount = 0

def trimStart(file):
    return ' '.join(file.split()[trimAmount:])

def appendStart(tempFile, count, ext):
    counterText = ""
    if appendTextIncrement:
        counterText = str(count) if count > 9 else '0' + str(count)
    
    return appendText + counterText + appendTextDivider + tempFile + ext

def printFileChanges(oldFileName, newFileName):
    print("\n  File renamed:")
    print("\n    - [" + oldFileName + "]")
    print("\n    + [" + newFileName + "]")

def rename():
    print("\nRenaming files ...")
    count = 1
    for file in os.listdir(path):
        if os.path.isdir(path + '\\' + file):
            continue
        
        tempFileName = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]

        tempFileName = trimStart(tempFileName)
        tempFileName = appendStart(tempFileName, count, ext)

        printFileChanges(file, tempFileName)
        
        newFileNamePath = path + '\\' + tempFileName
        oldFileNamePath = path + '\\' + file

        os.rename(os.path.join(oldFileNamePath), os.path.join(newFileNamePath))
        count += 1

rename()
