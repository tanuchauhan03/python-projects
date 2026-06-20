#file handling : file handling is way to store access and manipulate data in files on your computer .
#syntax :file=open("filename.txt","mode")

#reading from the file : we dont need to close the file explicitly it closed after read
with open(r"C:\Users\HP\Desktop\git-demo\python-projects\notes.txt","r") as file:
    content=file.read()
    print(content)