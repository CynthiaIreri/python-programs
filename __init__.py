import os, glob

os.chdir("/Users/Ireri/Desktop/pythonProject")
for file in glob.glob("*.txt"):
    print(file)
