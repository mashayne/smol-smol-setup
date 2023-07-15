```python
import requests
from smol_dev_wizard.utils import download_file, run_command

smol_dev_path = "/path/to/smol_dev"
download_success = "Smol Developer was successfully downloaded."

def download_smol_dev():
    smol_dev_url = "https://url.to/smol_dev.zip"
    download_file(smol_dev_url, smol_dev_path)
    print(download_success)

if __name__ == "__main__":
    download_smol_dev()
```