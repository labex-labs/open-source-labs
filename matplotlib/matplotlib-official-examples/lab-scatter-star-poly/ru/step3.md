# Создаем подграфики

Мы создадим сетку подграфиков 2x3 с использованием функции `subplots()`.

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
