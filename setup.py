#/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Dynamically calculate the version based on photologue.VERSION
version_tuple = __import__('photologue').VERSION
if len(version_tuple) == 3:
    version = "%d.%d.%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name='django-uuslug',
    version = version,
    description = "A Django slugify application that guarantees uniqueness and handles unicode",
    long_description = read('README'),
    author='Optim Informatique',
    author_email='mcordoquy@optiminformatique.fr',
    url='http://github.com/mcordoquy/django-uuslug',
    packages=['uuslug'],
    install_requires = ['Unidecode>=0.04.5'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )
