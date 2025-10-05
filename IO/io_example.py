#! /usr/bin/env python3

import sys

# Lendo o stream de entrada padrão
# 0 - STDIN
data = sys.stdin.readline()
print(f"Você digitou: {data}")

# Escrevendo nos streams
# 1 - STDOUT (saida padrão)
sys.stdout.write("Mensagem normal\n")
# 2 - STDERR (saida de erro)
sys.stderr.write("Mensagem de erro\n")


# run with: python3 io_example.py

# pipeline of splitting stdout and stderr
# python3 io_example.py > report.txt 2> error.txt
