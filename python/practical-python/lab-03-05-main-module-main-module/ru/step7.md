# Аргументы командной строки

Список аргументов командной строки представляет собой список текстовых строк.

```bash
$ python3 report.py portfolio.csv prices.csv
```

Этот список текстовых строк доступен в `sys.argv`.

```python
# В предыдущей bash-команде
sys.argv # ['report.py', 'portfolio.csv', 'prices.csv']
```

Вот простой пример обработки аргументов:

```python
import sys

if len(sys.argv)!= 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
