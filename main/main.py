import os
import shutil

BACKUP_PATH = "C:/Users/Sinjin/Desktop/Let That Sync In/backup folder [test]"


def start():
    fileName = 'testing.txt'
    filePath = BACKUP_PATH + "/" + fileName
    create_txt = open(filePath, 'w')
    create_txt.write("Testing content...")
    create_txt.close()

    checking_files = True
    while checking_files:
        cont = input('. . . To reset press -> [ r ] . . .\t')
        if cont.lower() == 'r':
            os.remove(filePath)
            checking_files = False
        else:
            print("\n! Incorrect Response !\n")

if __name__ == '__main__':
    start()
