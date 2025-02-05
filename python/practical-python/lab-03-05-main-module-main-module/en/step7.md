# Command Line Args

The command line is a list of text strings.

```bash
$ python3 report.py portfolio.csv prices.csv
```

This list of text strings is found in `sys.argv`.

```python
# In the previous bash command
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

Here is a simple example of processing the arguments:

```python
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
