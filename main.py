import os

source = "main.txt"
dest = "newfile.txt"
os.rename(source, dest)
print("Source path rename to the destination is successful")