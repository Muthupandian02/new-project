from setuptools import setup
from typing import List

def get_requirements(filepath:str)-> List[str]:
    with open(filepath: str = 'requiremnts.txt' 'r')  as file:
