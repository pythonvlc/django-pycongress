#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import pycongress


setup(
    name="pycongress",
    author="Marcos Gabarda",
    author_email="hey@marcosgabarda.com",
    version=pycongress.__version__,
    description="A collection of Django apps for a conference website.",
    long_description=open('README.rst', 'r').read(),
    url="https://github.com/pythonvlc/django-pycongress",
    packages=find_packages(),
    include_package_data=True,
    classifiers=(
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ),
    install_requires=open('requirements.txt', 'r').read().splitlines(),
)
