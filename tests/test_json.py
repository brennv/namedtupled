import namedtupled
import pytest
import os


FIXTURE_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'data',)

json_object = """
    {
      "foo": "bar",
      "baz": {"qux": "quux"},
      "tito": {
        "tata": "tutu",
        "totoro": "tots",
        "frobnicator": ["this", "is", "not", "a", "mapping"]},
      "alist": [{"one": "1", "a": "A"}, {"two": "2", "b": "B"}]
    }
"""

json_array = """
    [
      {
        "foo": "bar",
        "baz": {"qux": "quux"},
        "tito": {
          "tata": "tutu",
          "totoro": "tots",
          "frobnicator": ["this", "is", "not", "a", "mapping"]},
        "alist": [{"one": "1", "a": "A"}, {"two": "2", "b": "B"}]
      },
      {
        "foo": "bar",
        "baz": {"qux": "quux"},
        "tito": {
          "tata": "tutu",
          "totoro": "tots",
          "frobnicator": ["this", "is", "not", "a", "mapping"]},
        "alist": [{"one": "1", "a": "A"}, {"two": "2", "b": "B"}]
      }
    ]
"""


def test_namedtupled_json_object_memory(data=json_object):
    t = namedtupled.json(data)
    assert t.tito.tata == 'tutu'
    assert t.tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t.foo == 'bar'
    assert t.baz.qux == 'quux'
    assert t.alist[0].a == 'A'
    assert t.alist[1].two == '2'
    assert t.baz != {'qux': 'quux'}
    assert t.alist[0] != {'one': '1', 'a': 'A'}


def test_namedtupled_json_array_memory(data=json_array):
    t = namedtupled.json(data)
    assert t[0].tito.tata == 'tutu'
    assert t[0].tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t[0].foo == 'bar'
    assert t[0].baz.qux == 'quux'
    assert t[0].alist[0].a == 'A'
    assert t[0].alist[1].two == '2'
    assert t[0].baz != {'qux': 'quux'}
    assert t[0].alist[0] != {'one': '1', 'a': 'A'}


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'object.json'))
def test_namedtupled_json_object_file(datafiles):
    path = datafiles.listdir()[0]
    t = namedtupled.json(path=path)
    assert t.tito.tata == 'tutu'
    assert t.tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t.foo == 'bar'
    assert t.baz.qux == 'quux'
    assert t.alist[0].a == 'A'
    assert t.alist[1].two == '2'
    assert t.baz != {'qux': 'quux'}
    assert t.alist[0] != {'one': '1', 'a': 'A'}


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'array.json'))
def test_namedtupled_json_array_file(datafiles):
    path = datafiles.listdir()[0]
    t = namedtupled.json(path=path)
    assert t[0].tito.tata == 'tutu'
    assert t[0].tito.frobnicator == ['this', 'is', 'not', 'a', 'mapping']
    assert t[0].foo == 'bar'
    assert t[0].baz.qux == 'quux'
    assert t[0].alist[0].a == 'A'
    assert t[0].alist[1].two == '2'
    assert t[0].baz != {'qux': 'quux'}
    assert t[0].alist[0] != {'one': '1', 'a': 'A'}


def test_nametupled_json_error(data=json_object, path='foo.json'):
    with pytest.raises(ValueError) as e:
        namedtupled.json(data=data, path=path)
    'expected one source' in str(e)
