#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pycdlib']

setup_requirements = [ 

]

test_requirements = [ ]

setup(
    author="Stas Fomin",
    author_email='stas-fomin@yandex.ru',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Pack Folder to ISO and BZ",
    entry_points={
        'console_scripts': [
            'folder2iso=folder2iso.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='folder2iso',
    name='folder2iso',
    packages=find_packages(include=['folder2iso', 'folder2iso.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/belonesox/folder2iso',
    version='0.1.0',
    zip_safe=False,
)
