# Создание фигуры и подграфиков

Мы создадим фигуру с двумя подграфиками с использованием метода `add_gridspec`.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```
