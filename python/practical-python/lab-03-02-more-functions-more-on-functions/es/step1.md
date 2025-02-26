# Llamada a una función

Considere esta función:

```python
def read_prices(filename, debug):
  ...
```

Puede llamar a la función con argumentos posicionales:

    prices = read_prices('prices.csv', True)

O puede llamar a la función con argumentos de palabras clave:

```python
prices = read_prices(filename='prices.csv', debug=True)
```
