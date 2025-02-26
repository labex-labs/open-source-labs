# Arguments par défaut

Parfois, vous voulez qu'un argument soit facultatif. Dans ce cas, affectez-lui une valeur par défaut dans la définition de la fonction.

```python
def read_prices(filename, debug=False):
 ...
```

Si une valeur par défaut est assignée, l'argument est facultatif dans les appels de fonction.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_Nota : Les arguments avec des valeurs par défaut doivent apparaître à la fin de la liste d'arguments (tous les arguments non facultatifs vont en premier)._
