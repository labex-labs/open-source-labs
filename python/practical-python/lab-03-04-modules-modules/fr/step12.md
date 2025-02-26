# Exercice 3.11 : Importations de modules

Dans la section 3, nous avons créé une fonction générale `parse_csv()` pour analyser le contenu de fichiers de données au format CSV.

Maintenant, nous allons voir comment utiliser cette fonction dans d'autres programmes. Commencez par ouvrir une nouvelle fenêtre de terminal. Naviguez vers le dossier où se trouvent tous vos fichiers. Nous allons les importer.

Démarrez le mode interactif de Python.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Une fois que vous avez fait cela, essayez d'importer certains des programmes que vous avez précédemment écrits. Vous devriez voir leur sortie exactement comme avant. Pour souligner, importer un module exécute son code.

```python
>>> import bounce
... observez la sortie...
>>> import mortgage
... observez la sortie...
>>> import report
... observez la sortie...
>>>
```

Si rien de cela ne fonctionne, vous êtes probablement exécutant Python dans le mauvais répertoire. Maintenant, essayez d'importer votre module `fileparse` et d'obtenir de l'aide sur celui-ci.

```python
>>> import fileparse
>>> help(fileparse)
... regardez la sortie...
>>> dir(fileparse)
... regardez la sortie...
>>>
```

Essayez d'utiliser le module pour lire certaines données :

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... regardez la sortie...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... regardez la sortie...
>>> prices = dict(pricelist)
>>> prices
... regardez la sortie...
>>> prices['IBM']
106.28
>>>
```

Essayez d'importer une fonction pour ne pas avoir besoin d'inclure le nom du module :

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... regardez la sortie...
>>>
```
