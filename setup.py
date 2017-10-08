from setuptools import setup

setup(
    name='hue-sensors',
    version='1.0',
    py_modules=['hue_sensors'],
    url='https://github.com/robmarkcole/Hue-sensors',
    keywords='phillips hue',
    author='Robin Cole',
    author_email='robmarkcole@gmail.com',
    description='Tools for reading the state of Philips Hue sensors',
    install_requires=['requests'],
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"]
)
