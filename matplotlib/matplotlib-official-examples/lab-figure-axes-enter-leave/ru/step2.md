# Создание фигуры и осей

Мы создадим фигуру с двумя подграфиками (осями) с использованием функции `subplots`. Также зададим заголовок для фигуры.

```python
fig, axs = plt.subplots(2, 1)
fig.suptitle('Mouse Hover Over Figure or Axes to Trigger Events')
```
