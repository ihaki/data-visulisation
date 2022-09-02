from setuptools import setup, find_packages
setup(
    name = 'MeanStandardError',
    version = '0.1',
    packages = find_packages(exclude = ['tests']),
    licence = 'MIT',
    description = 'Mean standard error package',
    long_description = open('ReadMe.md').read(),
    install_requires = ['numpy', 'math'],
    url = "https://github.com/Ihaki/MeanStandardError",
    author = 'Pharis Ihaki',
    author_email = 'andrewpharisihaki@gmail.com'
 )