# Crear el gráfico

Ahora, podemos crear el gráfico sobre el que queremos superponer la imagen. En este ejemplo, crearemos un gráfico de barras simple utilizando datos aleatorios.

```python
fig, ax = plt.subplots()

np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()
```
