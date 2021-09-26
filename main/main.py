import os
import shutil
from utils import *

# static backup path for now will change to variable that user selects
backup_start = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In/backup start [test]"
backup_end = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In/backup end [test]"


def start():
    fileName = input("")
    newFile = create_txtFile(backup_start, fileName)
    usr1 = input("Would you like to copy the new file?(y/n)  -  ")
    file_src, file_dst = copy_file_to(newFile, backup_end)
    usr2 = input("Delete old backup file?(y/n)  -  ")
    del_file(file_src)


    #-------------------------------------------------------
    usr3 = input("Delete backup files for testing purposes....")
    file_dst = file_dst + "/" + fileName
    del_file(file_dst)



if __name__ == '__main__':
    start()
