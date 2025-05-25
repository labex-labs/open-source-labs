# Chamando uma Função

Considere esta função:

```python
def read_prices(filename, debug):
    ...
```

Você pode chamar a função com argumentos posicionais:

    prices = read_prices('prices.csv', True)

Ou você pode chamar a função com argumentos de palavra-chave (keyword arguments):

```python
prices = read_prices(filename='prices.csv', debug=True)
```
