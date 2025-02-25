# Crear el gráfico

Ahora que tenemos los datos, podemos crear el gráfico. Primero, creamos un objeto de figura y eje utilizando `plt.subplots()`. Luego, trazamos los datos utilizando `ax.plot()`.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```
