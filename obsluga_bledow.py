import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print("Removing {}".format(tmpfile_path))
        os.remove(tmpfile_path)

    print("Downloading url {}".format(url))
    save_url_to_file(url, tmpfile_path)

    print("Copying file {} {}".format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError as e:
    print("Invalid URL address")

except PermissionError as e:
    print("No permission for read-only files - please change the permission for {} file".format(file))

except FileNotFoundError as e:
    print("File {} not found".format(tmpfile))

except Exception as e:
    print("Sorry, the error has occured...\nDetails:\n{}".format(e))

else:
    print("URL downloaded successfully")

finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print("The file has been deleted")