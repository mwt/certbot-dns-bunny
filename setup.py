import os
import sys

from setuptools import find_packages
from setuptools import setup

version = '0.0.2'

install_requires = [
    'requests>=2.28.1',
    'setuptools>=41.6.0',
]

if not os.environ.get('SNAP_BUILD'):
    install_requires.extend([
        # We specify the minimum acme and certbot version as the current plugin
        # version for simplicity. See
        # https://github.com/certbot/certbot/issues/8761 for more info.
        f'acme>={version}',
        f'certbot>={version}',
    ])
elif 'bdist_wheel' in sys.argv[1:]:
    raise RuntimeError('Unset SNAP_BUILD when building wheels '
                       'to include certbot dependencies.')
if os.environ.get('SNAP_BUILD'):
    install_requires.append('packaging')

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

# Load readme to use on PyPI
with open('README.rst') as f:
    readme = f.read()

setup(
    name='certbot-dns-bunny',
    version=version,
    description="Bunny.net DNS Authenticator plugin for Certbot",
    url='https://github.com/mwt/certbot-dns-bunny',
    author="Matthew W. Thomas",
    author_email='certbot-dns-bunny@mwt.me',
    license='BSD-2-Clause',
    long_description = readme,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-bunny = certbot_dns_bunny._internal.dns_bunny:Authenticator',
        ],
    },
)
