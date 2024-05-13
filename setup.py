import os

from setuptools import setup, find_packages
setup_requirements = [
    'setuptools_scm>=8',
]
setup(
    name='buf_demo',
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=setup_requirements,
    nclude_package_data=True,
    package_data={'': ['protobuf/*']},
    install_requires=[
        'protobuf~=5.26',
        'betterproto==v2.0.0b6',
    ],

)
