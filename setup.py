from setuptools import setup
from typing import List

def get_requirements(filepath:str)-> List[str]:
    with open(filepath,'r')  as file:
        requirements=file.readlines()
        print(requirements)
        req=[lib.strip() for lib in requirements if lib.strip() != '-e .']
        return req
    
setup(
    name='---',
    version='1.1.1',
    author='Muthupandian',
    author_email='muthupandiansuresh2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)