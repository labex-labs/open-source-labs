# Mover las etiquetas de las marcas del eje X a la parte superior

Ahora que comprendemos la posición predeterminada de las etiquetas de las marcas, movamos las etiquetas de las marcas del eje x a la parte superior del gráfico.

## Comprender los parámetros de las marcas (Ticks)

Matplotlib proporciona el método `tick_params()` para controlar la apariencia de las marcas (ticks) y las etiquetas de las marcas. Este método nos permite:

- Mostrar/ocultar las marcas y las etiquetas de las marcas.
- Cambiar su posición (arriba, abajo, izquierda, derecha).
- Ajustar su tamaño, color y otras propiedades.

## Crear un gráfico con las etiquetas de las marcas del eje X en la parte superior

Creemos un nuevo gráfico con las etiquetas de las marcas del eje x movidas a la parte superior:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.cos(x)

# Plot the data
ax.plot(x, y, marker='s', linestyle='-', color='green', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',         # Apply changes to the x-axis
    top=True,         # Show ticks on the top side
    labeltop=True,    # Show tick labels on the top side
    bottom=False,     # Hide ticks on the bottom side
    labelbottom=False # Hide tick labels on the bottom side
)

# Add a title and labels
ax.set_title('Cosine Wave with X-Axis Tick Labels at the Top')
ax.set_xlabel('X-axis (now at the top!)')
ax.set_ylabel('Y-axis (cos(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Now the x-axis tick labels are at the top of the plot!")
```

Cuando ejecutes este código, verás un gráfico de onda cosenoidal con las etiquetas de las marcas del eje x en la parte superior del gráfico.

Observa cómo se utiliza el método `tick_params()` con varios parámetros:

- `axis='x'`: Especifica que queremos modificar el eje x.
- `top=True` y `labeltop=True`: Hace que las marcas y las etiquetas sean visibles en la parte superior.
- `bottom=False` y `labelbottom=False`: Oculta las marcas y las etiquetas en la parte inferior.

Esto nos da una vista clara de los datos con las etiquetas del eje x posicionadas en la parte superior en lugar de en la parte inferior.
