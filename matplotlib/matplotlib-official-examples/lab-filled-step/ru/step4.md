# Настраиваем функцию гистограммы с фиксированными интервалами

Мы настроим функцию гистограммы с фиксированными интервалами с использованием `numpy.histogram`. Мы создадим 20 интервалов, ranging от -3 до 3.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
