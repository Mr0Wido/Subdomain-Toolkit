#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

setup(
    name='subdomain_toolkit',
    version='0.1',
    author='Mr0Wido',
    author_email='mr0wido@protonmail.com',
    description='A collection of subdomain discovery tools',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'subdomain_toolkit=subdomain_toolkit.__main__:main'
        ]
    }
)

os.system("sudo apt-get install -y curl unzip")
os.system("sudo apt-get install -y sublist3r subfinder amass assetfinder")
os.system("curl -LO https://github.com/Findomain/Findomain/releases/download/8.2.2/findomain-linux.zip && unzip findomain-linux.zip  && rm findomain-linux.zip && chmod +x findomain && sudo mv findomain /usr/bin/findomain")
