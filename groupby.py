import os
import itertools

def scantree(path):
    for object in os.scandir(path):
        if object.is_dir():
            yield object
            yield from scantree(object.path)
        else:
            yield object

path = r'C:\Users\Ola\Desktop\Dokumenty'
listing = scantree(path)

for i in listing:
    print("Is object a directory: {}, is object a file: {}, path: {}".format(i.is_dir(), not(i.is_dir()), i.path))

data = sorted(listing, key = lambda x: x.is_dir())

for is_dir, elements in itertools.groupby(data, key = lambda x: x.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
