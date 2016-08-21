from future import standard_library
standard_library.install_aliases()
from collections import Mapping, namedtuple, UserDict


def mapper(mapping, name='NT'):
    """ Convert mappings to namedtuples recursively. """
    if isinstance(mapping, Mapping) and not isinstance(mapping, AsDict):
        for key, value in list(mapping.items()):
            mapping[key] = mapper(value)
        return namedtuple_wrapper(name, **mapping)
    elif isinstance(mapping, list):
        return [mapper(item) for item in mapping]
    return mapping


def namedtuple_wrapper(name, **kwargs):
    wrap = namedtuple(name, kwargs)
    return wrap(**kwargs)


class AsDict(UserDict):
    """ A class that exists just to tell `mapper` not to eat it. """


def ignore(mapping):
    """ Use ignore to prevent a mapping from being mapped to a namedtuple. """
    if isinstance(mapping, Mapping):
        return AsDict(mapping)
    elif isinstance(mapping, list):
        return [ignore(item) for item in mapping]
    return mapping
