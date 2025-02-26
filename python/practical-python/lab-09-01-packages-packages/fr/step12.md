# Exercice 9.2 : Création d'un répertoire d'application

Placer tout votre code dans un "package" n'est souvent pas suffisant pour une application. Parfois, il y a des fichiers d'assistance, de la documentation, des scripts et autres éléments. Ces fichiers doivent exister EN DEHORS du répertoire `porty/` que vous avez créé ci-dessus.

Créez un nouveau répertoire appelé `porty-app`. Déplacez le répertoire `porty` que vous avez créé dans l'Exercice 9.1 dans ce répertoire. Copiez les fichiers de test `portfolio.csv` et `prices.csv` dans ce répertoire. Créez également un fichier `README.txt` avec quelques informations sur vous-même. Votre code devrait maintenant être organisé comme suit :

    porty-app/
        portfolio.csv
        prices.csv
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

Pour exécuter votre code, vous devez vous assurer d'être dans le répertoire `porty-app/` de niveau supérieur. Par exemple, à partir du terminal :

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

Essayez d'exécuter certains de vos scripts antérieurs en tant que programme principal :

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
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
```
