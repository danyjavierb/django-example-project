import os

from .factory import *


SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, os.path.pardir, os.path.pardir))
REPO_DIR = os.path.abspath(os.path.join(PROJECT_DIR, os.path.pardir))

def project_dir(*args):
	"""
	Returns the absolute path of joined args with PROJECT_DIR.

	>>> PROJECT_DIR = '/path/to/project'
	>>> project_dir('foo', 'bar')
	'/path/to/project/foo/bar'
	"""
	return os.path.abspath(os.path.join(PROJECT_DIR, *args))

INSTALLED_APPS += (
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	'django.contrib.admindocs',
	'gunicorn',
)

PROJECT_APPS = (
	'example_project.core',
)
