# Creación de un Gráfico Básico con Datos Aleatorios

Antes de agregar la superposición de la imagen, necesitamos crear un gráfico que servirá como base para nuestra visualización. Vamos a crear un simple gráfico de barras utilizando datos aleatorios.

1. Crea una nueva celda en tu cuaderno (notebook) e introduce el siguiente código:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

Este código hace lo siguiente:

- Crea una figura y ejes con un tamaño específico utilizando `plt.subplots()`.
- Establece una semilla aleatoria para garantizar que obtengamos los mismos valores aleatorios cada vez que ejecutamos el código.
- Genera 30 valores en el eje x (desde 0 hasta 29) y los correspondientes valores en el eje y (x más ruido aleatorio).
- Crea un gráfico de barras con barras verdes utilizando `ax.bar()`.
- Agrega líneas de cuadrícula al gráfico con `ax.grid()`.
- Agrega etiquetas para el eje x, el eje y y un título para el gráfico.
- Utiliza `plt.tight_layout()` para ajustar el espaciado y mejorar la apariencia.
- Muestra el gráfico utilizando `plt.show()`.

2. Ejecuta la celda presionando Shift+Enter.

La salida debe mostrar un gráfico de barras con barras verdes que representan los datos aleatorios. El eje x muestra enteros del 0 al 29, y el eje y muestra los valores correspondientes con ruido aleatorio agregado.

Este gráfico será la base sobre la cual superpondremos nuestra imagen en el siguiente paso. Observa cómo hemos almacenado el objeto de la figura en la variable `fig` y el objeto de los ejes en la variable `ax`. Necesitaremos estas variables para agregar la superposición de la imagen.
