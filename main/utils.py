import os
import shutil
import random



#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")


def create_txtFile(backup_path):
    fileName = 'testing.txt'
    filePath = backup_path + "/" + fileName
    create_txt = open(filePath, 'w')
    create_txt.write("Testing content...")
    create_txt.close()
    return filePath


# shutil.copy(src, dst, *, follow_symlinks=True)
def copy_file_to(src, dst):
    shutil.copy(src, dst)


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
