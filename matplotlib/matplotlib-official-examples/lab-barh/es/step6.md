# Personalizar el gráfico

Para que el gráfico sea más informativo, podemos personalizarlo agregando etiquetas, título e invirtiendo el eje y.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
