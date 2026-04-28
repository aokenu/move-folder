import glob
import os
import shutil
import time
#get the unique variable to defferentiate date
date=input("enter date: yyyymmdd: ")
path1 = "C:/python_work/Billingsample/Billingsample/"
#path2="_040219"

#pad the full source path where the original file exist
src_folder=f"{path1}{date}"
dst_folder = f'C:/python_work/sample/3line Card management Limited_{date}_155959/ '
print(src_folder)

#make a list of the content of the source path
file_names