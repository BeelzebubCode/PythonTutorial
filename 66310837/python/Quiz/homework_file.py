import os

number = int(input())

if number % 2 == 0:
    result = number + 5
else:
    result = number - 5


desktop_path = "C:/Users/pongr/OneDrive/เดสก์ท็อป/test1"
file_path = os.path.join(desktop_path, "testFile1.txt")


os.mkdir(desktop_path) 
with open(file=file_path, mode="w") as file:
    file.write(f"{result}")