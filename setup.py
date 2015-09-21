import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


EXTRAS_REQUIRES = dict(
    parser=[
        # runtime version must match version of jar used to create the parser
        # and lexer
        'antlr_python_runtime==3.1.3',
    ],
    test=[
        'pytest>=2.5.1',
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
    version='0.1.0',
    description=(
        "Lightweight implementation of Google's Protocol Buffers in Python",
    ),
    long_description=long_description,
    author='Andres Buritica, Andres Gayton',
    author_email='andres@thelinuxkid.com, andy@thecablelounge.com',
    maintainer='Andy Gayton',
    maintainer_email='andy@thecablelounge.com',
    url='https://github.com/thelinuxkid/python-protolite',
    license='MIT',
    packages=find_packages(),
    cmdclass=dict([('test', PyTest)]),
    tests_require=['pytest>=2.5.1'],
    install_requires=[
        'setuptools',
        ],
    entry_points={
        'console_scripts': [
            'python-protolitec = protolite.cli.protolitec:main[parser]',
        ],
    },
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
