import os
import shutil

source = input("enter the file name you want to relocate: ")
destination = input("enter the name of the destination of the file: ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source+file), destination) 