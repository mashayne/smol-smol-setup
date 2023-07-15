```python
from utils import run_command

dependencies_list = [
    # Add the dependencies here in the format {"name": "dependency_name", "version": "dependency_version"}
]

def install_dependency(dependency):
    command = f"pip install {dependency['name']}=={dependency['version']}"
    run_command(command)
    print(f"Dependency {dependency['name']} installed successfully.")

def check_dependencies():
    for dependency in dependencies_list:
        try:
            importlib.import_module(dependency['name'])
        except ImportError:
            print(f"Dependency {dependency['name']} is not installed. Installing now...")
            install_dependency(dependency)
        else:
            print(f"Dependency {dependency['name']} is already installed.")
```