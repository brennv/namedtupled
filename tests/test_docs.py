import namedtupled
import pytest


def test_getting_started():
    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)
    assert cat.binks.says == 'meow'
    # cat = namedtupled.map(data, name='Cat')
    # cat  # Cat(binks=NT(says='meow'))


def test_map():
    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)
    assert cat.binks.says == 'meow'
    data = [{'id': 'binks', 'says': 'meow'}, {'id': 'cedric', 'says': 'prrr'}]
    cats = namedtupled.map(data)
    assert cats[1].says == 'prrr'


def test_zip():
    keys, values = ['id', 'says'], ['binks', 'prrr']
    cat = namedtupled.zip(keys, values)
    assert cat.says == 'prrr'


def test_json():
    data = """{"binks": {"says": "meow"}}"""
    cat = namedtupled.json(data)
    assert cat.binks.says == 'meow'
    # cat = namedtupled.json(path='cat.json')
    # assert cat.says == 'meow'


def test_yaml():
    # cat = namedtupled.yaml(path='cat.yaml')
    # assert cat.says == 'meow'
    data = """
    binks:
      says: meow
    """
    cat = namedtupled.yaml(data)
    assert cat.binks.says == 'meow'


# def test_env():
    # export USERNAME="binks"
    #export APIKEY="c4tnip!"
    # vars = ['USERNAME', 'APIKEY']
    # cat = namedtupled.env(vars)
    # assert cat.username == 'binks'


def test_ignore():
    data = {'binks': namedtupled.ignore({'says': 'meow'})}
    cat = namedtupled.map(data)
    assert cat.binks == {'says': 'meow'}
