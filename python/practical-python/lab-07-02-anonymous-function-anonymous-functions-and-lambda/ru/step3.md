# Lambda:анонимные функции

Используйте lambda вместо создания функции. В нашем предыдущем примере сортировки.

```python
portfolio.sort(key=lambda s: s['name'])
```

Это создает _безымянную_ функцию, которая вычисляет _единственное_ выражение. Код выше гораздо короче, чем исходный код.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# по сравнению с lambda
portfolio.sort(key=lambda s: s['name'])
```
