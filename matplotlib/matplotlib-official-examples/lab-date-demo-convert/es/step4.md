# Crear el gráfico

Ahora, podemos crear el gráfico utilizando las fechas y los valores de y. Primero crearemos un objeto de figura y eje utilizando la función subplots. Luego, trazaremos el gráfico utilizando la función plot. Copie y pegue el siguiente código:

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
