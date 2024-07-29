#!/usr/bin/python

from distutils.core import setup

UNITTESTS = [
		"basic",
	]

setup(name='Unidecode',
      version='0.04.16',
      description='ASCII transliterations of Unicode text',
      license='GPL',
      long_description=open("README").read(),
      author='Tomaz Solc',
      author_email='tomaz.solc@tablix.org',

      packages = [ 'unidecode' ],

      provides = [ 'unidecode' ],

      classifiers = [
	"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
	"Programming Language :: Python",
	"Programming Language :: Python :: 2",
	"Programming Language :: Python :: 3",
	"Topic :: Text Processing",
	"Topic :: Text Processing :: Filters",
	],
)
