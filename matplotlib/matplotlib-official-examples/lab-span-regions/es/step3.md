# Crear el gráfico

Ahora crearemos el gráfico utilizando `matplotlib.pyplot`. Graficaremos la onda senoidal y agregaremos una línea horizontal en y = 0.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```
