# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_hijri_datepicker/__init__.py
from frappe_hijri_datepicker import __version__ as version

setup(
	name='frappe_hijri_datepicker',
	version=version,
	description='The Hijri(Islamic) calendar is the official calendar in countries around the Gulf, especially Saudi Arabia.',
	author='Mostafa Mohamed',
	author_email='m.dev.odoo@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
