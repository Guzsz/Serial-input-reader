import os, shutil

# <make a file>
def makeafile(name):
    makefille = open(name, "w")

def readfile(name, data):
    readfile = open(name, "a")
    readfile.write( f"{data}\n")

def readlist(name, data):
    readfile = open(name, "a")
    readfile.writelines(data)

# < move a file >
def moveafile(path_move, namefile):
   true_path = os.path.abspath(str(namefile))
   shutil.move(true_path, path_move)






