from setuptools import setup, find_packages


from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='combine2xlsx',
	packages=['combine2xlsx'],
	version='0.1.7',
	install_requires=['xlrd', 'xlsxwriter'],
	description='Combine multi excel files into one large xlsx',
	long_description=long_description,
	license='MIT License',
	author='Zhongpu Chen',
	author_email='chenloveit@163.com',
	url = 'https://pypi.python.org/pypi/combine2xlsx',
	keywords='excel xlsx xls',
)