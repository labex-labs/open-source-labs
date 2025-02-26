# Appeler une fonction

Considérez cette fonction :

```python
def read_prices(filename, debug):
  ...
```

Vous pouvez appeler la fonction avec des arguments positionnels :

    prices = read_prices('prices.csv', True)

Ou vous pouvez appeler la fonction avec des arguments nommés :

```python
prices = read_prices(filename='prices.csv', debug=True)
```
