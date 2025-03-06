# Superposición de la Imagen en el Gráfico

Ahora que hemos creado nuestro gráfico base, vamos a superponer la imagen sobre él. Utilizaremos el método `figimage` para agregar la imagen a la figura, y la haremos semi-transparente para que el gráfico debajo siga siendo visible.

1. Crea una nueva celda en tu cuaderno (notebook) e introduce el siguiente código:

```python
# Create a figure and axes for our plot (same as before)
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
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

Este código combina lo que hicimos en los pasos anteriores y agrega el método `figimage` para superponer nuestra imagen en el gráfico. Aquí está un desglose de los parámetros de `figimage`:

- `im`: Los datos de la imagen como una matriz NumPy.
- `25, 25`: Las posiciones x e y en píxeles desde la esquina inferior izquierda de la figura.
- `zorder=3`: Controla el orden de dibujo. Los números más altos se dibujan encima de los elementos con números más bajos.
- `alpha=0.5`: Controla la transparencia de la imagen. Un valor de 0 es completamente transparente, y 1 es completamente opaco.

2. Ejecuta la celda presionando Shift+Enter.

La salida debe mostrar el mismo gráfico de barras que antes, pero ahora con el logotipo de Matplotlib superpuesto en la esquina inferior izquierda. El logotipo debe ser semi-transparente, permitiendo que el gráfico debajo siga siendo visible.

3. Vamos a experimentar con diferentes posiciones y niveles de transparencia. Crea una nueva celda e introduce el siguiente código:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

Este código coloca la imagen en el centro de la figura con un nivel de transparencia más alto (alpha = 0.3), lo que la hace más adecuada como marca de agua.

4. Ejecuta la celda presionando Shift+Enter.

La salida debe mostrar el gráfico de barras con el logotipo centrado y más transparente que antes, creando un efecto de marca de agua.
