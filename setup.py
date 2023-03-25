#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

setup(
    name='subdomain_toolkit',
    version='0.1',
    author='Mr0Wido',
    author_email='mr0wido@protonmail.com',
    keywords='subdomain dns detection',
    description='A collection of subdomain discovery tools',
    license='MIT',
    packages=find_packages()+['.'],
    include_package_data=True,
    install_requires=[
        'requests',
        'tqdm'
    ],

    entry_points={
        'console_scripts': [
            'subdomain_tool = subdomain_tool:interactive']
    },
    python_requires='>=3.6',
)

os.system("apt-get install -y curl unzip")
os.system("apt-get install -y sublist3r subfinder amass assetfinder")
os.system("apt-get update -y sublist3r")
os.system("curl -LO https://github.com/Findomain/Findomain/releases/download/8.2.2/findomain-linux.zip && unzip findomain-linux.zip  && rm findomain-linux.zip && chmod +x findomain && sudo mv findomain /usr/bin/findomain")
