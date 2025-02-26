# Exercice 3.17 : Passer de noms de fichiers à des objets similaires à des fichiers

Vous avez maintenant créé un fichier `fileparse.py` qui contenait une fonction `parse_csv()`. La fonction fonctionnait comme ceci :

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

En ce moment, la fonction attend qu'on lui passe un nom de fichier. Cependant, vous pouvez rendre le code plus flexible. Modifiez la fonction de sorte qu'elle fonctionne avec n'importe quel objet similaire à un fichier/itérable. Par exemple :

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

Dans ce nouveau code, que se passe-t-il si vous passez un nom de fichier comme avant?

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... regardez la sortie (elle devrait être folle)...
>>>
```

Oui, vous devrez faire attention. Pourriez-vous ajouter une vérification de sécurité pour éviter cela?
