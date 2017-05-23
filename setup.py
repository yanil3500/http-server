"""
setup for http-server
"""
from setuptools import setup

DEPENDENCIES = ['pytest', 'pytest-cov', 'ipython']
MODULES = ['server', 'client']
EXTRA_PACKAGES = {
    'test': ['tox']
}
CONSOLE_SCRIPTS = {
    'console_scripts': [
        'server = server:main'
        'client = client:main'
    ]
}
setup(
    name="http-server",
    description="""A simple HTTP server written in Python..""",
    version='0.1',
    author='Elyanil Castro, Erik Enderlein',
    author_email='yanil3500@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    # insert the names of pymodule into array
    py_modules=MODULES,
    install_requires=DEPENDENCIES,
    extras_require=EXTRA_PACKAGES,
    # console scripts allow for custom commands
    entry_points=CONSOLE_SCRIPTS


)