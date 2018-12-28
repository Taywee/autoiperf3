#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Absolute Performance, Inc
# Written by Taylor C. Richberger <taywee@gmx.com>

from setuptools import setup

from autoiperf3 import __version__, __description__

setup(
    name='autoiperf3',
    version=str(__version__),
    description=__description__,
    author='Taylor C. Richberger',
    author_email='taywee@gmx.com',
    url='https://github.com/Taywee/autoiperf3',
    license='GPLv3+',
    packages=[
        'autoiperf3',
        ],
    entry_points={
        'console_scripts': [
            'autoiperf3=autoiperf3.__main__:main',
        ],
    },
    install_requires=[
        'strictyaml',
        'paramiko',
        ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        ],
)
