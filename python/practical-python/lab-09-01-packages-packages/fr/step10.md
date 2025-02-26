# Structure d'application

L'organisation du code et la structure des fichiers sont clés pour la maintenabilité d'une application.

Il n'y a pas d'approche "unique" pour Python. Cependant, une structure qui fonctionne pour de nombreux problèmes est la suivante.

```code
porty-app/
  README.txt
  script.py         # SCRIPT
  porty/
    # CODE DE BIBLIOTHÈQUE
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Le niveau supérieur `porty-app` est un conteneur pour tout le reste - la documentation, les scripts de niveau supérieur, les exemples, etc.

Encore une fois, les scripts de niveau supérieur (s'il y en a) doivent exister en dehors du package de code. Un niveau au-dessus.

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

À ce stade, vous avez un répertoire avec plusieurs programmes :

    pcost.py          # calcule le coût d'un portefeuille
    report.py         # Génère un rapport
    ticker.py         # Génère un indice boursier en temps réel

Il existe une variété de modules d'assistance avec d'autres fonctionnalités :

    stock.py          # Classe Stock
    portfolio.py      # Classe Portfolio
    fileparse.py      # Analyse CSV
    tableformat.py    # Tableaux formatés
    follow.py         # Suivre un fichier de journal
    typedproperty.py  # Propriétés de classe typées

Dans cet exercice, nous allons nettoyer le code et le placer dans un package commun.
