# Генерируем случайные блуждания

Мы генерируем 40 случайных блужданий по 30 шагов каждый с использованием функции `random_walk()`, определенной ранее. Все случайные блуждания храним в списке под названием `walks`.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
