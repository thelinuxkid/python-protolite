#!/usr/bin/python
from setuptools import setup, find_packages
import os

EXTRAS_REQUIRES = dict(
    test=[
        'nose>=1.3.0',
        ],
    dev=[
        'ipython>=1.1.0',
        ],
    )

# Tests always depend on all other requirements, except dev
for k,v in EXTRAS_REQUIRES.iteritems():
    if k == 'test' or k == 'dev':
        continue
    EXTRAS_REQUIRES['test'] += v

# Pypi package documentation
root = os.path.dirname(__file__)
path = os.path.join(root, 'README.rst')
with open(path) as fp:
    long_description = fp.read()

setup(
    name='protolite',
    version='0.0.0.1',
    description=(
        "Lightweight implementation of Google's Protocol Buffers in Python",
    ),
    long_description=long_description,
    author='Andres Buritica',
    author_email='andres@thelinuxkid.com',
    maintainer='Andy Gayton',
    maintainer_email='andy@littleinc.com',
    url='https://github.com/littleinc/python-protolite',
    license='MIT',
    packages = find_packages(),
    test_suite='nose.collector',
    install_requires=[
        'setuptools',
        ],
    extras_require=EXTRAS_REQUIRES,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ],
)
