```python
import os
from smol_dev_wizard.requirements import requirements_list
from smol_dev_wizard.dependencies import dependencies_list
from smol_dev_wizard.utils import run_command

smol_dev_path = "/path/to/smol_dev"

def setup_smol_dev():
    os.makedirs(smol_dev_path, exist_ok=True)
    for requirement in requirements_list:
        install_requirement(requirement)
    for dependency in dependencies_list:
        install_dependency(dependency)
    print(setup_success)

def install_requirement(requirement):
    command = f"pip install {requirement['name']}=={requirement['version']}"
    run_command(command)
    print(requirement_install_success.format(requirement['name']))

def install_dependency(dependency):
    command = f"apt-get install {dependency['name']}=={dependency['version']}"
    run_command(command)
    print(dependency_install_success.format(dependency['name']))

setup_success = "Smol Developer was successfully set up."
requirement_install_success = "Requirement {} was successfully installed."
dependency_install_success = "Dependency {} was successfully installed."

if __name__ == "__main__":
    setup_smol_dev()
```