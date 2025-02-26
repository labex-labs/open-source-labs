# Tri de listes revisité

Les listes peuvent être triées _in-place_. En utilisant la méthode `sort`.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

Vous pouvez trier dans l'ordre inverse.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

Cela semble assez simple. Cependant, comment trier une liste de dictionnaires?

```python
[{'name': 'AA', 'price': 32.2,'shares': 100},
{'name': 'IBM', 'price': 91.1,'shares': 50},
{'name': 'CAT', 'price': 83.44,'shares': 150},
{'name': 'MSFT', 'price': 51.23,'shares': 200},
{'name': 'GE', 'price': 40.37,'shares': 95},
{'name': 'MSFT', 'price': 65.1,'shares': 50},
{'name': 'IBM', 'price': 70.44,'shares': 100}]
```

Selon quel critère?

Vous pouvez guider le tri en utilisant une _fonction clé_. La _fonction clé_ est une fonction qui reçoit le dictionnaire et renvoie la valeur d'intérêt pour le tri.

```python
portfolio = [
    {'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

Voici le résultat.

```python
# Vérifiez comment les dictionnaires sont triés par la clé `name`
[
  {'name': 'AA', 'price': 32.2,'shares': 100},
  {'name': 'CAT', 'price': 83.44,'shares': 150},
  {'name': 'GE', 'price': 40.37,'shares': 95},
  {'name': 'IBM', 'price': 91.1,'shares': 50},
  {'name': 'IBM', 'price': 70.44,'shares': 100},
  {'name': 'MSFT', 'price': 51.23,'shares': 200},
  {'name': 'MSFT', 'price': 65.1,'shares': 50}
]
```
