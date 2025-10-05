#! /usr/bin/env python3

with open(0) as stdin:
    content = stdin.read()
    lines = content.splitlines()

    print(f"Li {len(lines)} linhas")
    print(f"Total de {len(content)} caracteres")

# run with: python3 truque_open.py
# finish with: Ctrl+D

# examples of pipeline:
# cat app.env | python3 chunks.py
# cat chunks.py | python3 truque_open.py
