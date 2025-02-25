# Agregar etiquetas de eje y título

Agregaremos etiquetas de eje y un título al gráfico usando las funciones `plt.ylabel`, `plt.yticks`, `plt.xticks` y `plt.title`.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Pérdida en ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Pérdida por desastre')
```
