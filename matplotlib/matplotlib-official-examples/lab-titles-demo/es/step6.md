# Posicionamiento vertical manual

Especifica manualmente la posición vertical del título utilizando el parámetro `y` de la función `title()`.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```
