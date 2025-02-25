# Crear un gráfico de barras agrupadas

Ahora, podemos crear nuestro gráfico utilizando la función `bar` de Matplotlib. Crearemos un bucle que itere a través de nuestros atributos y cree un conjunto de barras para cada uno. También ajustaremos el ancho de las barras y la posición de cada conjunto de barras.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
