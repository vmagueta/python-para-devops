#! /usr/bin/env python3

import sys, json

config = {}
for line in sys.stdin:
    line = line.strip()
    if line and '=' in line:
        key, value = line.split('=', 1)
        config[key] = value

json.dump(config, sys.stdout, indent=2)


# run with:
# cat app.env | python3 env_to_json.py
