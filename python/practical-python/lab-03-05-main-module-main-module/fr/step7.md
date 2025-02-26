# Arguments de ligne de commande

La ligne de commande est une liste de chaînes de caractères textuelles.

```bash
$ python3 report.py portfolio.csv prices.csv
```

Cette liste de chaînes de caractères textuelles est trouvée dans `sys.argv`.

```python
# Dans la commande bash précédente
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

Voici un exemple simple de traitement des arguments :

```python
import sys

if len(sys.argv)!= 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
