from setuptools import find_packages, setup

setup(
    name='igenny',
    url='https://github.com/Constructionware/igenny.git',
    version='0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    
    install_requires=[
    'StringGenerator',
    ],
)

