
file = open(r"D:\filehandling\functiontypes.txt", "a")
file.write("Are Function Types\n")
file.close()


file = open(r"D:\filehandling\functiontypes.txt", "r")
print(file.read())
file.close()
