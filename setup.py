import os
import sys
import json

from setuptools import setup, find_packages


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='hive_kernel',
      version='0.4.0',
      description='A hive kernel for Jupyter.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/Hourout/hive_kernel',
      author='JinQing Lee',
      author_email='hourout@163.com',
      keywords=['jupyter_kernel', 'hive_kernel'],
      license='Apache License Version 2.0',
      install_requires=['pyhive', 'sqlalchemy', 'pandas', 'jupyter'],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: System :: Shells',
      ],
      packages=['hive_kernel'],
      zip_safe=False
)
