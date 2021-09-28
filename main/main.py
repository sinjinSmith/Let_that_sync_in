import os
import shutil
from utils import *

def start():
    #explore("C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In")
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    #folder_path = filedialog.askdirectory()


    fileName = input("Enter name for a new file  -  ")

    print("Choose directory for file to be created in...")
    file_location = filedialog.askdirectory()

    newFile = create_txtFile(file_location, fileName)

    usr1 = input("Would you like to backup the new file?(y/n)  -  ")
    if usr1.lower() == 'y':
        print("Choose directory to backup file to...")
        dirPath = filedialog.askdirectory()
        file_src, file_dst = copy_file_to(newFile, dirPath)


    usr2 = input("Delete old backup file?(y/n)  -  ")
    if usr2.lower() == 'y':
        del_file(file_src)


    #-------------------------------------------------------
    usr3 = input("Delete all new files for testing purposes?(y/n) - ")
    file_dst = file_dst + "/" + fileName
    if usr3.lower() == 'y':
        del_file(file_dst)




if __name__ == '__main__':
    start()
