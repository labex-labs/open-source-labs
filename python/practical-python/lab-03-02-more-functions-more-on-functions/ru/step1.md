# Вызов функции

Рассмотрим эту функцию:

```python
def read_prices(filename, debug):
 ...
```

Вы можете вызывать функцию с позиционными аргументами:

    prices = read_prices('prices.csv', True)

Или вы можете вызывать функцию с именованными аргументами:

```python
prices = read_prices(filename='prices.csv', debug=True)
```
