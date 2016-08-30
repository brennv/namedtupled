import namedtupled
import pytest


mapping = {
    'foo': 'bar',
    'baz': {'qux': 'quux'},
    'tito': {
        'tata': 'tutu',
        'totoro': 'tots',
        'frobnicator': ['this', 'is', 'not', 'a', 'mapping']
    },
    'alist': [{'one': '1', 'a': 'A'}, {'two': '2', 'b': 'B'}]
}

mapping_array = [mapping, mapping]


def test_namedtupled_map_object(mapping=mapping):
    t = namedtupled.map(mapping)
    d = namedtupled.reducer(t)
    assert d['tito']['tata'] == 'tutu'
    assert d['tito']['frobnicator'] == ['this', 'is', 'not', 'a', 'mapping']
    assert d['foo'] == 'bar'
    assert d['baz']['qux'] == 'quux'
    assert d['alist'][0]['a'] == 'A'
    assert d['alist'][1]['two'] == '2'
    assert d['baz'] == {'qux': 'quux'}
    assert d['alist'][0] == {'one': '1', 'a': 'A'}


def test_namedtupled_map_array(mapping=mapping_array):
    t = namedtupled.map(mapping)
    d = namedtupled.reducer(t)
    assert d[0]['tito']['tata'] == 'tutu'
    assert d[0]['tito']['frobnicator'] == ['this', 'is', 'not', 'a', 'mapping']
    assert d[0]['foo'] == 'bar'
    assert d[0]['baz']['qux'] == 'quux'
    assert d[0]['alist'][0]['a'] == 'A'
    assert d[0]['alist'][1]['two'] == '2'
    assert d[0]['baz'] == {'qux': 'quux'}
    assert d[0]['alist'][0] == {'one': '1', 'a': 'A'}
