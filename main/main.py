import os
import shutil

BACKUP_PATH = "C:/Users/Sinjin/Desktop/Let That Sync In/backup folder [test]"

#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")


def start():
    fileName = 'testing.txt'
    filePath = BACKUP_PATH + "/" + fileName
    create_txt = open(filePath, 'w')
    create_txt.write("Testing content...")
    create_txt.close()

    checking_files = True
    while checking_files:
        cont = input('. . . To reset press -> [ r ] . . .')
        if cont.lower() == 'r':
            os.remove(filePath)
            checking_files = False
        else:
            print("! Incorrect Response !")

if __name__ == '__main__':
    start()
