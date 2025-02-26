# Определение функций

Хорошей идеей является размещение всего кода, связанного с одной _задачей_, в одном месте. Используйте функцию.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Функция также упрощает повторяющиеся операции.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
