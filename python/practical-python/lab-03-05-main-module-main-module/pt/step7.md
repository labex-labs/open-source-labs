# Argumentos da Linha de Comando

A linha de comando é uma lista de strings de texto.

```bash
$ python3 report.py portfolio.csv prices.csv
```

Esta lista de strings de texto é encontrada em `sys.argv`.

```python
# No comando bash anterior
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

Aqui está um exemplo simples de processamento dos argumentos:

```python
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
