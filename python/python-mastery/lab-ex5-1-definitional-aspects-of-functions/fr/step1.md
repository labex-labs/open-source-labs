# Préparation

Dans l'exercice 2.6, vous avez écrit un module `reader.py` qui avait une fonction pour lire un fichier CSV dans une liste de dictionnaires. Par exemple :

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

Plus tard, nous avons étendu ce code pour qu'il fonctionne avec des instances dans l'exercice 3.3 :

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

Finalement, le code a été refactorisé en une collection de classes impliquant l'héritage dans l'exercice 3.7. Cependant, le code est devenu assez complexe et embrouillé.
