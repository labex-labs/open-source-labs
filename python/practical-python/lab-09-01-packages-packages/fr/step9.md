# Une autre solution pour les scripts

Comme indiqué, vous devez désormais utiliser `-m package.module` pour exécuter les scripts dans votre package.

```bash
$ python3 -m porty.pcost portfolio.csv
```

Il existe une autre alternative : écrire un nouveau script de niveau supérieur.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

Ce script se trouve _en dehors_ du package. Par exemple, en examinant la structure de répertoire :

    pcost.py       # script de niveau supérieur
    porty/         # répertoire du package
        __init__.py
        pcost.py
     ...
