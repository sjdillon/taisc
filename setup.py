from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    requirements = file.readlines()

setup(name='taisctaisc',
      version='0.1',
      description='helps record streaming radio',
      url='https://github.com/sjdillon/taisc',
      author='sjdillon',
      author_email='sjdillon',
      license='MIT',
      packages=find_packages(),
      install_requires=requirements,
      zip_safe=True)
