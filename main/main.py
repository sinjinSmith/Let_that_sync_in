import os
import shutil
from utils import *

# static backup path for now will change to variable that user selects
backup_start = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In/backup start [test]"
backup_end = "C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In/backup end [test]"


def start():
    create_txtFile(backup_start)
    newFile = create_txtFile(backup_start)
    usr1 = input("Would you like to copy the new file?(y/n)  -  ")
    copy_file_to(newFile, backup_end)



if __name__ == '__main__':
    start()
