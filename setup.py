from setuptools import setup, find_packages
packages = ['mymodules'] #'src', 

for p in packages:
    setup(
        name = p,
        packages = find_packages()
    )