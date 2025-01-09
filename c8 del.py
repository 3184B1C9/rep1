import os

filePath = "file.txt"
i = input("Want to delete file [yes/no]:").strip().lower()

if i == "yes":
    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("file doesn't exist")
else:
    print("Not deleteing")

