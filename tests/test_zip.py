import namedtupled
import pytest


keys = ['foo', 'baz', 'tito', 'alist']

values = [
    'bar',
    {'qux': 'quux'},
    {
        'tata': 'tutu',
        'totoro': 'tots',
        'frobnicator': ['this', 'is', 'not', 'a', 'mapping']
    },
    [
        {'one': '1', 'a': 'A'},
        {'two': '2', 'b': 'B'}
    ]
]


def test_namedtupled_zip(keys=keys, values=values):
    t = namedtupled.zip(keys, values)
    assert t.tito.tata == 'tutu'
    assert t.tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t.foo == 'bar'
    assert t.baz.qux == 'quux'
    assert t.alist[0].a == 'A'
    assert t.alist[1].two == '2'
    assert t.baz != {'qux': 'quux'}
    assert t.alist[0] != {'one': '1', 'a': 'A'}
