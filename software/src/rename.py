from distutils import extension
import shutil
import os

#desviation in blender por center iris x=88.3 y=0.863
lvl = "L1"
dire = "C"
dir = f"src/img/{dire}/{lvl}/"
files = os.listdir(dir)
H = 0
V = f"{dire}{lvl}-"
center = 30
total = 60
initio = 0
extension = "png"
pos_int = 4



for key in range(len(files)):
    name_prev=(files[key].split('V')[1])
    #name_prev=files[key]

    name = f"{V}{name_prev}"
    print(name)
    shutil.move(dir + files[key],dir +name)

