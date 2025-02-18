# Título en la parte superior

Crea un gráfico con el título en la parte superior utilizando la función `subplots()` y la función `set_xlabel()`.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```
