import os
import shutil
import random
from tkinter import filedialog
import tkinter
import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
#explore("C:/Users/Sinjin/Desktop/Pythonic Works/!Active Projects/Let That Sync In")

#tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
#folder_path = filedialog.askdirectory()

#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#os.mkdir(path, mode=0o777, *, dir_fd=None)     -   create new directories

# shutil.copy(src, dst, *, follow_symlinks=True)
def copy_file_to(src, dst):
    shutil.copy(src, dst)
    return src, dst

#os.rmdir(path, *, dir_fd=None)
def del_dir(path):
        os.rmdir(path)

def del_file(path):
    os.remove(path)

def create_txtFile(backup_path, fileName):
    filePath = backup_path + "/" + fileName
    create_txt = open(filePath, 'w')
    create_txt.write("Testing content...")
    create_txt.close()
    return filePath

# --------------------------------------------------------------

def find_all_files():
    #search through backup to check/find all directories/files
    pass

def validate_path():
    #confirm last known path is still valid
    pass

def create_backup_path():
    #create new backup directory/location
    pass

def push_backup():
    #erase old backup entirely and create a new one
    pass

def sync_backup():
    #check files and then push/overwrite newly edited or added files only
    pass
