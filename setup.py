from setuptools import setup,find_packages
from typing import List

HYPHAN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i  in requirements]

        if HYPHAN_E_DOT in requirements:
            requirements.remove(HYPHAN_E_DOT)
    
    return requirements

setup(
    name="income_prediction",
    version="0.1",
    author="Jyoti Kapoor",
    author_email="jyotikpr999@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)