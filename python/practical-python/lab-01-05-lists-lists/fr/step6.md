# Listes et mathématiques

_Attention : Les listes ne sont pas conçues pour les opérations mathématiques._

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

Plus précisément, les listes ne représentent pas des vecteurs/matrices comme dans MATLAB, Octave, R, etc. Cependant, il existe des packages pour vous aider dans ce domaine (par exemple, [numpy](https://numpy.org)).

Dans cet exercice, nous expérimentons le type de données liste de Python. Dans la dernière section, vous avez travaillé avec des chaînes de caractères contenant des symboles d'actions.

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

Divisez-la en une liste de noms en utilisant l'opération `split()` des chaînes de caractères :

```python
>>> symlist = symbols.split(',')
```
