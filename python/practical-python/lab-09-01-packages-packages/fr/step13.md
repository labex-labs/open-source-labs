# Exercice 9.3 : Scripts de niveau supérieur

Utiliser la commande `python -m` est souvent un peu étrange. Vous pouvez vouloir écrire un script de niveau supérieur qui traite simplement les particularités des packages. Créez un script `print-report.py` qui produit le rapport ci-dessus :

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Placez ce script dans le répertoire `porty-app/` de niveau supérieur. Assurez-vous de pouvoir l'exécuter à cet emplacement :

    $ cd porty-app
    $ python3 print-report.py portfolio.csv prices.csv txt
          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

    $

Votre code final devrait maintenant être structuré comme ceci :

    porty-app/
        portfolio.csv
        prices.csv
        print-report.py
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py
