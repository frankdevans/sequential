from setuptools import find_packages, setup


with open('./requirements.txt', 'r') as r: DEPENDENCIES = r.readlines()


setup(
	name = 'sequential',
	packages = find_packages(exclude = ['tests', 'tests.*']),
	package_data = {
		'': ['*.json'],  # If any package contains *.json files, include them
	},
	setup_requires = ['wheel'],
	install_requires = DEPENDENCIES,
	version = '0.0.0',
	description = 'Core validation and transpiling module for the Sequential data language.',
	author = 'Frank D. Evans',
)