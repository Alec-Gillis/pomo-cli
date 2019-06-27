# Ties all modules together and tells Python how to handle it

from setuptools import setup

setup(
	name = 'pycli',
	version = '0.1.0',
	packages = ['pycli'],
	entry_points = {
		'consol_scripts': [
			'pycli = pycli.__main__:main'
		]
	})
