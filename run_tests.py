# -*- coding: utf-8 -*-
#    Asymmetric Base Framework :: Jinja utils
#    Copyright (C) 2013-2014 Asymmetric Ventures Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import locale
import sys


try:
	import django #@UnusedImport
except ImportError:
	print("Error: django is required to run tests")
	sys.exit(1)

try:
	import jinja2 #@UnusedImport
except ImportError:
	print("Error: jinja2 is required to run tests")
	sys.exit(1)

try:
	import six #@UnusedImport
except ImportError:
	print("Error: six is required to run tests")
	sys.exit(-1)

def main():
	from django.conf import settings
	
	settings.configure(
		INSTALLED_APPS = (
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.admin',
			'django.contrib.sessions',
			'asymm_jinja'
		),
		DATABASE_ENGINE = 'django.db.backends.sqlite3',
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': ':memory:',
			}
		},
		DEBUG = True,
		USE_I18N = True,
		USE_L10N = True,
		LANGUAGE_CODE = 'en-us',
		TEMPLATE_DEBUG = True,
	)
	if django.get_version() >= '1.7':
		django.setup() #@UndefinedVariable
	
	apps = ['asymm_jinja']
	if django.get_version() >= '1.6':
		apps.append('asymm_jinja.tests')
	
	locale.setlocale(locale.LC_ALL, 'en_US.utf8')
	
	from django.test.utils import get_runner
	
	failures = get_runner(settings)(verbosity = 2, interactive = True).run_tests(apps)
	sys.exit(failures)

if __name__ == '__main__':
	main()
