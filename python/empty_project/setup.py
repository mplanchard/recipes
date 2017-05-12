"""
setup module for ihiji_schemas
"""

from os.path import dirname, join, realpath
from setuptools import setup, find_packages


NAME = 'INSERT NAME'
URL = ''
AUTHOR = 'INSERT AUTHOR'
EMAIL = ''

SHORT_DESC = ''
LONG_DESC = (
)
KEYWORDS = [
]

PACKAGE_DEPENDENCIES = [
]
SETUP_DEPENDENCIES = [
    'pytest-runner',
]
TEST_DEPENDENCIES = [
    'ipdb',
    'pytest',
    'pytest-cov',
]
EXTRAS_DEPENDENCIES = {}

ENTRY_POINTS = {}

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for all
# available setup classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    # 'Development Status :: 5 - Production/Stable',
    # 'Environment :: Web Environment',
    'Intended Audience :: Developers'
    # 'License :: Other/Proprietary License',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
]


__version__ = '0.0.0'

cwd = dirname(realpath(__file__))

with open(join(cwd, '{0}/_version.py'.format(NAME))) as version_file:
    for line in version_file:
        # This will populate the __version__ and __version_info__ variables
        if line.startswith('__'):
            exec(line)

setup(
    name=NAME,
    version=__version__,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    install_requires=PACKAGE_DEPENDENCIES,
    setup_requires=SETUP_DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    extras_require=EXTRAS_DEPENDENCIES,
)
