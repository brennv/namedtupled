import namedtupled
import pytest


mapping = {
    'foo': 'bar',
    'baz': {'qux': 'quux'},
    'tito': {
        'tata': 'tutu',
        'totoro': 'tots',
        'frobnicator': ['this', 'is', 'not', 'a', 'mapping']},
    'alist': [{'one': '1', 'a': 'A'}, {'two': '2', 'b': 'B'}],
    'huh': [('a', 'b', 'c')],
    'huh2': ('a', 'b', ('a', 'b', 'c')),
    'name': 'Bob'
}

mapping_array = [mapping, mapping]


def test_namedtupled_map_object(mapping=mapping):
    t = namedtupled.map(mapping)
    assert t.tito.tata == 'tutu'
    assert t.tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t.foo == 'bar'
    assert t.baz.qux == 'quux'
    assert t.alist[0].a == 'A'
    assert t.alist[1].two == '2'
    assert t.baz != {'qux': 'quux'}
    assert t.alist[0] != {'one': '1', 'a': 'A'}
    assert t.huh == [('a', 'b', 'c')]
    assert t.huh2 == ('a', 'b', ('a', 'b', 'c'))
    assert t.name == 'Bob'


def test_namedtupled_map_array(mapping=mapping_array):
    t = namedtupled.map(mapping)
    assert t[0].tito.tata == 'tutu'
    assert t[0].tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t[0].foo == 'bar'
    assert t[0].baz.qux == 'quux'
    assert t[0].alist[0].a == 'A'
    assert t[0].alist[1].two == '2'
    assert t[0].baz != {'qux': 'quux'}
    assert t[0].alist[0] != {'one': '1', 'a': 'A'}
