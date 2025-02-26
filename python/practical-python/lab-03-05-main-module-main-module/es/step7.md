# Argumentos de línea de comandos

La línea de comandos es una lista de cadenas de texto.

```bash
$ python3 report.py portfolio.csv prices.csv
```

Esta lista de cadenas de texto se encuentra en `sys.argv`.

```python
# En el comando bash anterior
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

A continuación se presenta un ejemplo simple de procesamiento de los argumentos:

```python
import sys

if len(sys.argv)!= 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
