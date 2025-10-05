#! /usr/bin/env python3

import sys, json, yaml

data = json.load(sys.stdin)
yaml.dump(data, sys.stdout, default_flow_style=False)

# run with:
# cat app.env | python3 env_to_json.py | python3 json_to_yaml.py
