#! /usr/bin/env python3

import sys, yaml, base64

data = yaml.safe_load(sys.stdin)
secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "data": {
        k: base64.b64encode(v.encode())
        for k, v in data.items()
    }
}

yaml.dump(secret, sys.stdout)

# run with:
# cat app.env | python3 env_to_json.py | python3 json_to_yaml.py | python3 yaml_to_k8s.py > secret.yaml
