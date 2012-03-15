# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

install_requires = [
    'django-cms>=2.1.3',
    'django-sekizai',
    'django-filer>=0.8.6',
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-filer-html5video",
    version = "0.1",
    url = 'https://github.com/piquadrat/cmsplugin-filer-html5video',
    license = 'BSD',
    description = "HTML5 video plugin for django CMS and django-filer, using VideoJS",
    long_description = read('README.rst'),
    author = 'Benjamin Wohlwend',
    author_email = 'piquadrat@gmail.com',
    packages = find_packages(),
    install_requires = install_requires,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        ],
    include_package_data=True,
    zip_safe = False
)