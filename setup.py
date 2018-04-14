#!/usr/bin/env python3
"""Simple deploy installer"""

from setuptools import find_packages, setup

with open('requirements.txt', 'rt') as reqs_file:
    REQUIREMENTS = reqs_file.readlines()

setup(
    name='deploy',
    description='Deploy amis to aws.',
    long_description=open('README.rst').read(),
    author='Bek',
    author_email='bek@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    setup_requires=['setuptools_scm'],
    use_scm_version={'local_scheme': 'dirty-tag'},
    install_requires=REQUIREMENTS,
    include_package_data=True,
    keywords="challenge",
    url='https://github.com/bazimov/simple_deploy',
    download_url='https://github.com/bazimov/simple_deploy',
    platforms=['OS Independent'],
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'deploy=deploy.__main__:main'
            ]},
    )
