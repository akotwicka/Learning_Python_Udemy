import os
import zipfile
import requests

class FileFromWeb:
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        self.response = requests.get(self.url)
        with open(self.tmp_file, "wb") as file:
            file.write(self.response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>>>>>>>>>> Error details',exc_type, exc_val, exc_tb)
        if exc_type == KeyError:
            print('>>>>> There is no file in archive! {}'.format(exc_val))
            return True
        elif exc_type == FileNotFoundError:
            print('>>>>> Incorrect directory/file: {}'.format(exc_val))
            return  True
        else:
            return False

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
tmp_file = "c:/temp/euroxref.zip"

with FileFromWeb(url, tmp_file) as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir("c:/temp")
        z.extract(a_file, ".", None)