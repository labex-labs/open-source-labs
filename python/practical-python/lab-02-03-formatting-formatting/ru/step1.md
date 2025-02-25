# Форматирование строк

Одним из способов форматирования строк в Python 3.6+ являются `f-строки`.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

Часть `{expression:format}` заменяется.

Она обычно используется с `print`.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
