from setuptools import find_namespace_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will returns the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]


        return requirements
    



setup(
    name='student_project',
    version='0.0.1',
    author='SK',
    author_email='sachinkadnor10@gmail.com',
    packages=find_namespace_packages(),
    install_requires=get_requirements('requirements.txt')
)