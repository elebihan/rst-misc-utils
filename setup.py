# -*- coding: utf-8 -*-
#
# rst-misc-utils - Miscellaneous restructuredText Tools
#
# Copyright (c) 2013 Eric Le Bihan <eric.le.bihan.dev@free.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
import glob

setup(name='rst-misc-utils',
      version='0.1.0',
      description='Miscellaneous tools for restructuredText files',
      long_description='''
      This is a collection of tools for handling restructuredText
      files.
      ''',
      license='GPLv3',
      url='https://github.com/elebihan/rst-misc-utils/',
      platforms=['Any'],
      keywords=['rst', 'code generator'],
      install_requires=['docutils'],
      scripts=[glob.glob('scripts/*')],
      author='Eric Le Bihan',
      author_email='eric.le.bihan.dev@free.fr')

# vim: ts=4 sts=4 sw=4 sta et ai
