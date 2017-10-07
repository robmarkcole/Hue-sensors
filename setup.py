"""Setup hue_sensors.py module.
See:
https://github.com/pypa/sampleproject/blob/master/setup.py
"""

from setuptools import setup
from codecs import open
import os

__version__ = '0.8'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = read('requirements.txt').split()

setup(
    name='hue_sensors',
    version=__version__,
    py_modules=['hue_sensors'],
    url='https://github.com/robmarkcole/Hue-sensors',
    keywords='hue',
    author='Robin Cole',
    author_email='robmarkcole@gmail.com',
    description='Tools for reading the state of Philips Hue sensors',
    long_description=read('README.md'),
    install_requires=requirements,
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"]
)
