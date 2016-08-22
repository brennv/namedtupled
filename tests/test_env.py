import namedtupled
import pytest


def test_env():
    # In shell first:
    # export USERNAME="binks"
    # export APIKEY="c4tnip!"
    # Or run:
    # source ./tests/setenv.sh
    variables = ['USERNAME', 'APIKEY']
    cat = namedtupled.env(variables)
    assert cat.USERNAME == 'binks'
