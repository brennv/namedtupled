from setuptools import setup


brief_description = """
.. image:: https://travis-ci.org/brennv/namedtupled.svg?branch=master
    :target: https://travis-ci.org/brennv/namedtupled
.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5-blue.svg
.. image:: https://img.shields.io/codecov/c/github/brennv/namedtupled.svg
    :target: https://codecov.io/gh/brennv/namedtupled

Source: `https://github.com/brennv/namedtupled`_

Docs: `https://namedtupled.readthedocs.io`_

`namedtuples`_ are immutable, performant and classy. **namedtupled** is
a lightweight wrapper for recursively creating namedtuples from nested
dicts, lists, json and yaml. Inspired by `hangtwenty`_.

Installation
============

.. code:: bash

    pip install namedtupled

Getting started
===============

.. code:: python

    import namedtupled

    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)

    cat  # NT(binks=NT(says='meow'))

    cat.binks.says  # 'meow'

.. _namedtuples: https://docs.python.org/3/library/collections.html
.. _hangtwenty: https://gist.github.com/hangtwenty/5960435
.. _https://github.com/brennv/namedtupled: https://github.com/brennv/namedtupled
.. _https://namedtupled.readthedocs.io: https://namedtupled.readthedocs.io
"""


setup(
    name='namedtupled',
    packages=['namedtupled'],
    version='0.3.4',
    description='Lightweight namedtuple wrapper for attribute-style data access (a la JavaScript objects).',
    long_description=brief_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    author='brennv',
    author_email='brennan@beta.build',
    license='MIT',
    url='https://github.com/brennv/namedtupled',
    download_url='https://github.com/brennv/namedtupled/tarball/0.3.3',
    keywords='namedtupled namedtuple json yaml attribute style data access javascript objects',
    install_requires=[
        'future==0.18.2',
        'pyyaml==6.0',
    ],
    include_package_data=True,
    zip_safe=False)
