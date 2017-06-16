#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(

    name='lazy_logger',
    version="0.1.2",
    description='provide a better logging',
    long_description=open('README.md').read(),
    author='lazy_logger',
    url='https://github.com/Python-Logging-For-Human/ezlogging',
    author_email='tim.yellow@gmail.com',
    license='MIT',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['lazy_logger'],


)
