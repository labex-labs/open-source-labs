# Crear el gráfico

A continuación, crearemos el gráfico utilizando la función `subplots()` de Matplotlib y graficaremos el precio de cierre ajustado de las acciones de Google en el tiempo.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
