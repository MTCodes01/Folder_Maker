# import library
import os
from time import sleep
os.mkdir("D:\\Project")           #Main Path
Dir = ["Beginners", "Intermediate", "Advanced"] #Folder names here
x = 0
with open("File.txt", "r") as fh: #File having all the names of files
    data = fh.read().split("&")   #Put & on the end of one folder files
for i in data:                    #Length of Folder = Length of sections in file of files
    j = i.split("\n")
    path = f"D:\\Project\\{Dir[x]}" # Put Path here
    os.mkdir(path)
    sleep(1)
    for k in j:
        with open(f"D:\\Project\\{Dir[x]}\\{k}.py", "w"):
            continue
    x += 1