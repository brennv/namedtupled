from mapper.mapper import mapper, ignore
from mapper.integrations import load_json, load_yaml, load_lists, load_env


namedtupled = mapper({'map': mapper, 'ignore': ignore, 'json': load_json,
        'yaml': load_yaml, 'zip': load_lists, 'env': load_env})
