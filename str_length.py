import os

path = r'C:\Users\Ola\Desktop\tekst.txt'

if os.path.isfile(path):
    a = open(path).read()
    b = len(a.split(sep = " "))
    print('There is {} words in this file.'.format(b))

result = os.path.isfile(path) and print('There is {} words in this file.'.format(len(open(path).read().split(sep = " "))))
