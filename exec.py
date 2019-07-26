import os

files_to_process = [
    r"C:\Users\Ola\PycharmProjects\Udemy\1.py",
    r"C:\Users\Ola\PycharmProjects\Udemy\2.py"]

for file in files_to_process:
    print(file)
    source = open(file).read()
    exec(source)
