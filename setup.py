from setuptools import setup, find_packages

setup(
    name='password_creator',
    version='1.1.1',
    license='MIT',
    description='Create a password using an URL',

    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/password_creator',

    packages=find_packages(exclude=('tests', 'docs')),

    install_requires=['pytest', 'pytest-qt'],
    tests_require=['pytest', 'pytest-qt'],
)
