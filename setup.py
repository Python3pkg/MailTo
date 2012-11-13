#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

from mailto import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mailto',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['mailto'],
    url='https://github.com/whardier/MailTo',
    license='MIT',
    description='Tornado based RELP server (standard and inetd sockets)',
    long_description=read('README'),
    install_requires=[
        'bottle>=0.11',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    entry_points={
        'console_scripts': [
            'mailtoserver = mailto.__init__:run_server',
        ],
    }
)


