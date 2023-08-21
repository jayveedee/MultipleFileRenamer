import os
import sys

class Renamer:

    path = ''
    fullPath = ""
    folderName = ""
    renameType = ""
    stripAmount = ""
    textToAdd = ""
    textToAddExtra = ""

    def __init__(self, folderName, renameType):
        self.folderName = folderName
        self.renameType = renameType
        self.fullPath = self.path + folderName
        if renameType == "m":
            self.stripAmount = sys.argv[3]
            self.textToAdd = sys.argv[4] 
            try:
                self.textToAddExtra = sys.argv[5] 
            except (IndexError) (ValueError):
                pass
        elif renameType == "v":
            try:
                self.stripAmount = sys.argv[3]
            except (IndexError) (ValueError):
                pass

    def rename(self):
        counter = 1
        for file in os.listdir(self.fullPath):
            newFileName, ext, currentFileName, currentFileNameSpilt = self.getFileParts(file)
            if self.renameType == "v":
                newFileName += self.createVideoFileNameFormat(newFileName, counter)
            elif self.renameType == "m":
                newFileName = self.createMusicFileNameFormat(newFileName, currentFileNameSpilt)
            self.printResult(currentFileName, newFileName, ext)

            newFileName += ext
            counter += 1

            os.rename(os.path.join(self.fullPath, currentFileName + ext),os.path.join(self.fullPath, newFileName))
    
    def getFileParts(self, file):
        newFileName = ""
        currentFileName = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]
        currentFileNameSpilt = currentFileName.split()
        return newFileName, ext, currentFileName, currentFileNameSpilt

    def createVideoFileNameFormat(self, newFileName, counter):
        newFileName = "EP"
        if counter > 9:
            newFileName += str(counter) + " - "
        else:
            newFileName += "0" + str(counter) + " - "
        return newFileName
    
    def createMusicFileNameFormat(self, newFileName, currentFileNameSpilt):
       currentFileNameSpilt = self.removeCopyText(currentFileNameSpilt)
       for i in range(len(currentFileNameSpilt)):
            if i < int(self.stripAmount):
               continue
            if i == int(self.stripAmount):
                newFileName += self.textToAdd + " "
            else:
                if self.textToAddExtra != "":
                    newFileName += currentFileNameSpilt[i] + " " + self.textToAddExtra
                else:
                    newFileName += currentFileNameSpilt[i]

    def removeCopyText(self, currentFileNameSpilt):
        copyText = currentFileNameSpilt[len(currentFileNameSpilt) - 2] + " " + currentFileNameSpilt[len(currentFileNameSpilt) - 1]
        if copyText in "- Copy":
            currentFileNameSpilt.pop()
            currentFileNameSpilt.pop()

    def printResult(self, currentFileName, newFileName, ext):
        newFileName += ext
        currentFileName += ext
        print("\nRenamed from -[" + currentFileName + "]")
        print("Renamed to   +[" + newFileName + "]")



renamer = Renamer(sys.argv[1], sys.argv[2])
renamer.rename()
