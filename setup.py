from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='fdircleaner_ar',
    version='0.0.3',
    description='Clean user folder by files extensions',
    long_description = long_description,
    url='http://github.com/dummy_user/useful',
    author='Arkadiy Sherstiuk',
    author_email='shervard99@gmail.com',
    license='MIT',
    packages= find_packages(where='src'),
    package_dir= {'':'src'},
    install_requires = ['regex'],
    python_requires = '>=3',
    entry_points = {'console_scripts': ['cleanfold = clean_folder:clean']}
    )
