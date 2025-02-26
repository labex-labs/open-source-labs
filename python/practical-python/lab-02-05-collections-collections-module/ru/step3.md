# Пример: отображения "один - много"

Проблема: вы хотите сопоставить ключ с несколькими значениями.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

Как и в предыдущем примере, вместо этого ключ `IBM` должен иметь два разных кортежа.

Решение: используйте `defaultdict`.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

`defaultdict` гарантирует, что каждый раз, когда вы обращаетесь к ключу, вы получаете значение по умолчанию.
