from setuptools import setup,find_packages
from typing import List
import os

HYFEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)
        
        return requirements

setup(
    name='AWS-CI-CD-Pipeline',
    verison='0.0.1',
    author='krunal',
    author_email='krunalp1908@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)