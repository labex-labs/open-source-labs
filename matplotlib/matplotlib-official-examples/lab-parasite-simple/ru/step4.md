# Добавление данных

Мы добавим данные на график с использованием функции `plot`. Каждую линию мы присвоим переменной, чтобы впоследствии можно было сослаться на нее.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```
