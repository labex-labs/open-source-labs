# Crear el gráfico

Vamos a crear un gráfico de líneas simple con algunas etiquetas de eje y largas.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
