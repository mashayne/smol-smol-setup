```python
# smol_dev_wizard/requirements.py

requirements_list = [
    # Add the requirements for Smol Developer here.
    # Each requirement should be a dictionary with 'name' and 'version' keys.
    # For example: {'name': 'requirement1', 'version': '1.0.0'}
]

def install_requirement(requirement):
    from utils import run_command

    command = f"pip install {requirement['name']}=={requirement['version']}"
    run_command(command)

    print(f"Requirement {requirement['name']} installed successfully.")

def check_requirements():
    for requirement in requirements_list:
        try:
            install_requirement(requirement)
            print(f"Requirement {requirement['name']} checked.")
        except Exception as e:
            print(f"Failed to install requirement {requirement['name']}. Error: {str(e)}")
            return False

    return True
```