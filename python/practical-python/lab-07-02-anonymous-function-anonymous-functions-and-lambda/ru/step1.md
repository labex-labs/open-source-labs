# Сортировка списков, revisited

Списки можно сортировать _на месте_. С использованием метода `sort`.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

Можно сортировать в обратном порядке.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

Похоже, все достаточно просто. Однако, как отсортировать список словарей?

```python
[{'name': 'AA', 'price': 32.2,'shares': 100},
{'name': 'IBM', 'price': 91.1,'shares': 50},
{'name': 'CAT', 'price': 83.44,'shares': 150},
{'name': 'MSFT', 'price': 51.23,'shares': 200},
{'name': 'GE', 'price': 40.37,'shares': 95},
{'name': 'MSFT', 'price': 65.1,'shares': 50},
{'name': 'IBM', 'price': 70.44,'shares': 100}]
```

По какому критерию?

Можно управлять сортировкой, используя _функцию-ключ_. _Функция-ключ_ — это функция, которая получает словарь и возвращает значение, по которому будет производиться сортировка.

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

Вот результат.

```python
# Проверить, как словари отсортированы по ключу `name`
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
