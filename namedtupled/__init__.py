from .mapper import mapper, ignore
from .integrations import load_json, load_yaml, load_lists, load_env


map = mapper
json = load_json
yaml = load_yaml
zip = load_lists
env = load_env
