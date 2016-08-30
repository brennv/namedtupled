import namedtupled
import pytest


mapping = {
    'foo': 'bar',
    'baz': {'qux': 'quux'},
    'tito': {
        'tata': 'tutu',
        'totoro': 'tots',
        'frobnicator': ['this', 'is', 'not', 'a', 'mapping']},
    'alist': [{'one': '1', 'a': 'A'}, {'two': '2', 'b': 'B'}]
}

mapping_array = [mapping, mapping]


def test_namedtupled_ignore_object(mapping=mapping):
    mapping = namedtupled.ignore(mapping)
    t = namedtupled.map(mapping)
    assert t == mapping


def test_nametupled_ignore_array(mapping=mapping_array):
    mapping = namedtupled.ignore(mapping)
    t = namedtupled.map(mapping)
    assert t == mapping
