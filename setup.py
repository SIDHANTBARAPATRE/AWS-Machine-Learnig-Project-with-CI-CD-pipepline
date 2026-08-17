from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        '''
        actually when python reads the it automatically adds the line break,
        after every line ...so we need to remove that...so we use .replace,
        to replace "\n" with "".
        '''

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



setup(
    name = "mlproject",
    version="0.0.1",
    author = "Sidhant",
    author_email = "sidhantbarapatre12@gmail.com",
    packages = find_packages(),
    install_packages = get_requirements('requirements.txt')
)