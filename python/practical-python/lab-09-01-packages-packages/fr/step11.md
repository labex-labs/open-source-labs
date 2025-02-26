# Exercice 9.1 : Création d'un package simple

Créez un répertoire appelé `porty/` et placez tous les fichiers Python ci-dessus à l'intérieur. Créez également un fichier `__init__.py` vide et placez-le dans le répertoire. Vous devriez avoir un répertoire de fichiers comme ceci :

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

Supprimez le fichier `__pycache__` qui se trouve dans votre répertoire. Celui-ci contient des modules Python pré-compilés antérieurement. Nous voulons commencer avec un état vierge.

Essayez d'importer certains des modules du package :

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

Si ces importations échouent, accédez au fichier approprié et corrigez les importations de module pour inclure une importation relative au package. Par exemple, une instruction telle que `import fileparse` pourrait devenir la suivante :

    # report.py
    from. import fileparse

...

Si vous avez une instruction telle que `from fileparse import parse_csv`, changez le code en :

    # report.py
    from.fileparse import parse_csv

...
