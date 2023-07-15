```python
import os
import urllib.request

def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        return True
    except Exception as e:
        print(f"Error while downloading file: {e}")
        return False

def run_command(command):
    try:
        os.system(command)
        return True
    except Exception as e:
        print(f"Error while running command: {e}")
        return False
```