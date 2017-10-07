from setuptools import setup

__version__ = '0.9'

setup(
    name='hue_sensors',
    version=__version__,
    py_modules=['hue_sensors'],
    url='https://github.com/robmarkcole/Hue-sensors',
    keywords='hue',
    author='Robin Cole',
    author_email='robmarkcole@gmail.com',
    description='Tools for reading the state of Philips Hue sensors',
    install_requires=['logging',
                      'pprint',
                      'requests'],
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"]
)
