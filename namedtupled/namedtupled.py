
from collections import namedtuple, UserDict
import platform
from future import standard_library
standard_library.install_aliases()


class VersionCheck:
    def compareVersion(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
ob1 = VersionCheck()


if (ob1.compareVersion(platform.python_version(),"3.10.0")) >= 0:
	from collections.abc import Mapping
elif (ob1.compareVersion(platform.python_version(),"3.10.0")) == -1:
	from collections import Mapping
    
    
def mapper(mapping, _nt_name='NT'):
    """ Convert mappings to namedtuples recursively. """
    if isinstance(mapping, Mapping) and not isinstance(mapping, AsDict):
        for key, value in list(mapping.items()):
            mapping[key] = mapper(value)
        return namedtuple_wrapper(_nt_name, **mapping)
    elif isinstance(mapping, list):
        return [mapper(item) for item in mapping]
    return mapping


def namedtuple_wrapper(_nt_name, **kwargs):
    wrap = namedtuple(_nt_name, kwargs)
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


def isnamedtupleinstance(x):  # thank you http://stackoverflow.com/a/2166841/6085135
    _type = type(x)
    bases = _type.__bases__
    if len(bases) != 1 or bases[0] != tuple:
        return False
    fields = getattr(_type, '_fields', None)
    if not isinstance(fields, tuple):
        return False
    return all(type(i)==str for i in fields)


def reducer(obj):
    if isinstance(obj, dict):
        return {key: reducer(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [reducer(value) for value in obj]
    elif isnamedtupleinstance(obj):
        return {key: reducer(value) for key, value in obj._asdict().items()}
    elif isinstance(obj, tuple):
        return tuple(reducer(value) for value in obj)
    else:
        return obj
