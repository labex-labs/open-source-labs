# Creando el gráfico de barras

Ahora estamos listos para crear nuestro gráfico de barras. Comenzaremos definiendo algunas variables que nos ayudarán a establecer el ancho de las barras y su posición en el eje x.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

A continuación, crearemos una figura y un objeto de eje utilizando el método `subplots()`. Luego, usaremos un bucle for para iterar a través de cada valor en nuestro conjunto de datos y crear una barra para cada uno.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

Establecemos el parámetro `bottom` en `0.001` para evitar tener barras con una altura de 0, lo cual no es compatible con una escala logarítmica.
