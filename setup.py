from setuptools import setup, find_packages

setup(
    name='libtestpip',
    version='0.1.0',
    packages=find_packages(),
    package_data={},
    author='Kevin Landreth',
    author_email='crackerjackmack@gmail.com',
    description='bug testing',
    include_package_data=False,
    install_requires=[
        'pipvoid',
    ],
    dependency_links=[
        'git+ssh://git@github.com/crackerjackmack/python-pip-source-3@master#egg=pipvoid-0',
    ],
    entry_points='''
    '''
)
