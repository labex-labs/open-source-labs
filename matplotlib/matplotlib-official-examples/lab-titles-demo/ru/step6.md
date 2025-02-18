# Ручная вертикальная позиция

Ручно укажите вертикальную позицию заголовка, используя параметр `y` функции `title()`.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```
