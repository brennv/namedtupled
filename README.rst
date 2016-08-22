.. image:: https://travis-ci.org/brennv/namedtupled.svg?branch=master
    :target: https://travis-ci.org/brennv/namedtupled
.. image:: https://img.shields.io/badge/python-2.7%2C3.5-blue.svg

namedtupled
===========

`namedtuples`_ are immutable, performant and classy. **namedtupled** is
a lightweight wrapper for recursively creating namedtuples from nested
dicts, lists, json and yaml. Inspired by `hangtwenty`_.

Installation
------------

.. code:: bash

    pip install namedtupled

Getting started
---------------

.. code:: python

    import namedtupled

    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)

    cat  # NT(binks=NT(says='meow'))

    cat.binks.says  # 'meow'

Usage
-----

Create namedtuples with methods: `map`_, `json`_, `yaml`_, `zip`_,
`env`_ and helper method `ignore`_.

Optionally name namedtuples by passing a ‘name’ argument to any method,
the default name is simply ‘NT’.

.. code:: python

    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data, name='Cat')

    cat  # Cat(binks=NT(says='meow'))

map()
~~~~~

Recursively convert mappings like nested dicts, or lists of dicts, into
to namedtuples.

*args: mapping, name=‘NT’*

From dict:

.. code:: python

    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)

    cat.bink.says  # 'meow'

From list:

.. code:: python

    data = [{'id': 'binks', 'says': 'meow'}, {'id': 'cedric', 'says': 'prrr'}]
    cats = namedtupled.map(data)

    cats[1].says  # 'prrr'

json()
~~~~~~

Map namedtuples from json data.

*args: data=None, path=None, name=‘NT’*

Inline:

.. code:: python

    data = """{"binks": {"says": "meow"}}"""
    cat = namedtupled.json(data)

    cat.binks.says  # 'meow'

Or specify path for a json file:

.. code:: python

    cat = namedtupled.json(path='cat.json')

    cat.binks.says  # 'meow'

yaml()
~~~~~~

Map namedtuples from yaml data.

*args: data=None, path=None, name=‘NT’*

Inline:

.. code:: python

    data = """
    binks:
      says: meow
    """
    cat = namedtupled.yaml(data)

    cat.binks.says  # 'meow'

Or specify path for a yaml file:

.. code:: python

    cat = namedtupled.yaml(path='cat.yaml')

    cat.binks.says  # 'meow'

zip()
~~~~~

Map namedtuples given a pair of key, value lists.

*args: keys=[], values=[], name=‘NT’*

Example:

.. code:: python

    keys, values = ['id', 'says'], ['binks', 'prrr']
    cat = namedtupled.zip(keys, values)

    cat.says  # 'prrr'

env()
~~~~~

Returns a namedtuple from a list of environment variables. If not found
in shell, gets input with *input* or *getpass*.

*args: keys=[], name=‘NT’, use\_getpass=False*

In shell:

.. code:: bash

    export USERNAME="binks"
    export APIKEY="c4tnip!"

Then in python:

.. code:: python

    variables = ['USERNAME', 'APIKEY']
    env = namedtupled.env(variables)

    env.username  # 'binks'

ignore()
~~~~~~~~

Use ignore to prevent a mapping from being converted to a namedtuple.

*args: mapping*

Example usage:

.. code:: python

    data = {'binks': namedtupled.ignore({'says': 'meow'})}
    cat = namedtupled.map(data)

    cat.binks  # {'says': 'meow'}

Development
-----------

PRs welcome, tests run with:

.. code:: bash

    pip install pytest pytest-cov pytest-datafiles
    python -m pytest --cov=namedtupled/ tests

.. _namedtuples: https://docs.python.org/3/library/collections.html
.. _hangtwenty: https://gist.github.com/hangtwenty/5960435
.. _map: #map
.. _json: #json
.. _yaml: #yaml
.. _zip: #zip
.. _env: #env
.. _ignore: #ignore
