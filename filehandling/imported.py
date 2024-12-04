file= open(r"D:\filehandling\functiontypes.txt","r")
content=file.read()
print(content)
with open(r"D:\filehandling\testfile.txt","a") as file:
     print(file.write(content))  
