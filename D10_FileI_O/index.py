import os

# Basic or Classic Flow of File
# Open
# Read, Write, and Append
# Close

# For reading a file
# read()
file = open("index.txt", "r")
content = file.read()
print(content)
file.close()

# readline() : read one line
file1 = open("index.txt", "r")
readLine = file1.readline()
print(readLine)
file1.close()

# readlines() : it reads all the line as list
file2 = open("index.txt", "r")
readLines = file2.readlines()
print(readLines)
file2.close()

# Best Practice: Looping Line by Line (not need to use close())
with open("index.txt", "r") as file3:
    for line in file3:
        print(line.strip())

# For writing a file
# write (): it overwrites the content
# writeFile = open("index.txt", "w")
# write1 = writeFile.write("Hello fellas")
# print(write1)  # gives the char no.
# writeFile.close()

# # read the file but this time we can see the overwritten content
# fileOpen = open("index.txt", "r")
# readFile = fileOpen.read()
# print(readFile)
# fileOpen.close()

# Best Approch
with open("index.txt", "w") as wrtFile:
    char_written = wrtFile.write("Hello!\nI am BSc.IT student")

print(char_written)

with open("index.txt", "r") as rdFile:
    print(rdFile.read())

# For append in a file or files
# Append()
with open("index.txt", "a") as appFile:
    appendFile = appFile.write("\nhello everyone\nI am Sashi Bhushan Yadav")

with open("index.txt", "r") as appRead:
    print(appRead.read())

# for r+
with open("data.txt", "r+") as f:
    print(f.read())
    f.write("\nAdded using r+")
# print(f.read)

# for w+
with open("data.txt", "w+") as f:
    f.write("Fresh content")
    f.seek(3)
    print(f.read())

# for a+
with open("data.txt", "a+") as f:
    f.write("\nAppended line")
    f.seek(0)
    print(f.read())

# For binary file
# with open("image.png", "rb") as f:
#     binary_data = f.read()

# Deleting a File
# 1st Way
# Safe way
if os.path.exists("fke.txt"):
    os.remove("fke.txt")
    print("File deleted")
else:
    print("File not found")

# Professional Way
try:
    os.remove("data2.txt")
    print("File deleted")
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("Permission denied")


