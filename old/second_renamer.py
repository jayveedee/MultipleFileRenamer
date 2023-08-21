import os
import sys
import re

class Renamer:
    
    path = 'D:'
    renameType = 'v'
    trim = False

    def __init__(self, renameType, shouldTrim):
        if renameType == 'v' or renameType == 'm':
            self.renameType = renameType
        if shouldTrim == "1":
            self.trim = True

    def rename(self):
        folderRenameResult = []
        for folder in os.listdir(self.path):
            fileRenameResult = []
            opedRenameResult = []

            folderContentPath = self.path + folder + '\\'

            episodeNumber = 1
            for file in os.listdir(folderContentPath):
                if os.path.isdir(folderContentPath + file + '\\'):
                    continue

                initalFileName = file
                resultingFileName = ""

                if self.renameType == 'v':
                    resultingFileName = self.setVideoFormat(file, episodeNumber)
                elif self.renameType == 'm':
                    resultingFileName = self.setMusicFormat(file)

                fileRenameResult.append([initalFileName, resultingFileName])
                episodeNumber += 1

                filePath = folderContentPath + file
                resultPath = folderContentPath + resultingFileName

                os.rename(os.path.join(filePath), os.path.join(resultPath))

            folderRenameResult.append([folder, fileRenameResult, opedRenameResult])

        self.printResult(folderRenameResult)

    def setMusicFormat(self, file):
        return "teststst"

    def setVideoFormat(self, file, episodeNumber):
        result = ""
        name = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]

        episodeText = "EP"
        episodeText += str(episodeNumber) if episodeNumber > 9 else "0" + str(episodeNumber)

        if self.trim == True:
            newName = name
            nameList = name.split(" ")
            trimEndIndex = -1
            for i in range(len(nameList)):
                if nameList[i].upper() == "EPISODE" or nameList[i].upper() == "EP" or nameList[i] == "-":
                    trimEndIndex = i + 1
                    if len(nameList) > i + 1 and nameList[i + 1].isnumeric():
                        if len(nameList) > i + 2 and nameList[i + 2] == "-":
                            trimEndIndex = i + 2 + 1
                        else:
                            trimEndIndex = i + 1 + 1
                    if len(nameList) > 1 + 1 and nameList[i + 1].upper() == "EPISODE" or nameList[i].upper() == "EP":
                        continue
                    else:
                        break
            if trimEndIndex != -1:
                newName = name.split(" ", trimEndIndex)[1]
            result = episodeText + " - " + newName + ext
        else:
            result = episodeText + " - " + ext

        return result

    def printResult(self, renameResult):
        for folderRenameResult in renameResult:
            print("\nRenaming folder \"" + folderRenameResult[0] + "\" ...")
            
            for renameResult in folderRenameResult[1]:
                print("\n     File Renamed from \"" + renameResult[0] + "\" to \"" + renameResult[1] + "\"")

            for renameResult in folderRenameResult[2]:
                print("\n          File Renamed from \"" + renameResult[0] + "\" to \"" + renameResult[1] + "\"")
            
            print("\n------------------------------------------------------")

try:
    renamer = Renamer(sys.argv[1], sys.argv[2])
    renamer.rename()
except IndexError:
    pass

