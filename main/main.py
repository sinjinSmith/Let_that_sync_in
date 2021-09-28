import os
import shutil
from utils import *

# static backup path for now will change to variable that user selects
backup_start = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In/backup start [test]"
backup_end = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In/backup end [test]"
dir1 = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In"

def start():
    fileName = input("Enter name for a new file  -  ")
    newFile = create_txtFile(backup_start, fileName)


    dirName = input("Enter new dir name  -  ")
    dirPath = dir1 + "/" + dirName 
    new_dir(dirPath)

    usr1 = input("Would you like to copy the new file?(y/n)  -  ")
    if usr1.lower() == 'y':
        file_src, file_dst = copy_file_to(newFile, dirPath)


    usr2 = input("Delete old backup file?(y/n)  -  ")
    if usr2.lower() == 'y':
        del_file(file_src)


    #-------------------------------------------------------
    usr3 = input("Delete all new file/folders for testing purposes?(y/n) - ")
    file_dst = file_dst + "/" + fileName
    if usr3.lower() == 'y':
        del_file(file_dst)
        del_dir(dirPath)




if __name__ == '__main__':
    start()
