"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from setuptools import Command, find_packages, setup
from skontol import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

with open(join(this_dir, 'requirements.txt'), encoding='utf-8') as fp:
    install_requires = fp.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['pytest', '--cov=neo', '-vv'])
        raise SystemExit(errno)


setup(
    name='skontol',
    version=__version__,
    description='skontol from kontol',
    long_description=long_description,
    url='https://github.com/IrfanDect/skontol',
    author='stytyd',
    author_email='stytyd@gmail.com',
    license='join now',
    install_requires=[
        'setuptools','docopt'
    ],
    classifiers=[
        'Intended Audience :: Developers', 'Topic :: Utilities',
        'License :: Public Domain', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='skontol_cli',
    include_package_data=True,
    packages=find_packages(exclude=['docs', 'tests*']),
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov', 'pytest-ordering','rich',
                 'testfixtures'],
    },
    entry_points={
        'console_scripts': [
            'skontol=skontol.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
