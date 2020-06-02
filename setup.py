from setuptools import setup

setup(
    name='ci_demo',

    version='0.1',

    description='Demonstration of setting up continuous integration for a Python project',

    url='https://github.com/OxfordRSE/ci-demo',

    author='Fergus Cooper',

    author_email='fergus.cooper@cs.ox.ac.uk',

    license='MIT',

    packages=['ci_demo'],

    install_requires=[
    ],

    extras_require={
        'docs': [
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8',
        ],
    },

    zip_safe=False
)
