from setuptools import setup
from setuptools import find_packages


setup(
    name='stockprice',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ], 
    version='0.0.0',
    entry_points='''
        [console_scripts]
        stockprice=stockprice.stockprice:stockprice
    '''
)