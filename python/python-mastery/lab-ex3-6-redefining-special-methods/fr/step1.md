# Meilleure représentation pour la présentation d'objets

Tous les objets Python ont deux représentations sous forme de chaîne de caractères. La première représentation est créée par la conversion en chaîne via `str()` (qui est appelée par `print`). La représentation sous forme de chaîne est généralement une version bien formatée de l'objet destinée aux humains. La seconde représentation est une représentation de code de l'objet créée par `repr()` (ou simplement en visualisant une valeur dans l'interpréteur interactif). La représentation de code montre généralement le code que vous devez taper pour obtenir l'objet. Voici un exemple qui illustre l'utilisation de dates :

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # utilise str()
2008-07-05
>>> d    # utilise repr()
datetime.date(2008, 7, 5)
>>>
```

Il existe plusieurs techniques pour obtenir la chaîne `repr()` dans la sortie :

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
>>>
```

Modifiez l'objet `Stock` que vous avez créé de manière à ce que la méthode `__repr__()` produise une sortie plus utile. Par exemple :

```python
>>> goog = Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Voyez ce qui se passe lorsque vous lisez un portefeuille d'actions et que vous visualisez la liste résultante après avoir effectué ces modifications. Par exemple :

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23),
 Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
>>>
```
