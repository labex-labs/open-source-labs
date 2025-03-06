# Guardar y compartir tu gráfico

El último paso es guardar tu gráfico personalizado para que puedas incluirlo en informes, presentaciones o compartirlo con otros.

## Guardar gráficos en diferentes formatos

Matplotlib te permite guardar gráficos en varios formatos, incluyendo PNG, JPG, PDF, SVG y más. Aprendamos cómo guardar nuestro gráfico en diferentes formatos:

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

Cuando ejecutes este código, el gráfico se guardará en tres formatos diferentes:

- PNG: Un formato de imagen rasterizado adecuado para la web y uso general.
- PDF: Un formato vectorial ideal para publicaciones e informes.
- SVG: Un formato vectorial excelente para la web y gráficos editables.

Los archivos se guardarán en el directorio de trabajo actual de tu cuaderno de Jupyter.

## Comprender los parámetros de guardado

Examinemos los parámetros utilizados con `savefig()`:

- `dpi=300`: Establece la resolución (puntos por pulgada) para formatos rasterizados como PNG.
- `bbox_inches='tight'`: Ajusta automáticamente los límites de la figura para incluir todos los elementos sin espacio en blanco innecesario.

## Ver los archivos guardados

Puedes ver los archivos guardados navegando al explorador de archivos en Jupyter:

1. Haz clic en el logotipo de "Jupyter" en la esquina superior izquierda.
2. En el explorador de archivos, deberías ver los archivos de imagen guardados.
3. Haz clic en cualquier archivo para verlo o descargarlo.

## Opciones adicionales de exportación de gráficos

Para tener más control sobre el gráfico guardado, puedes personalizar el tamaño de la figura, ajustar el fondo o cambiar la resolución (DPI) según tus necesidades:

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

Esto demuestra cómo guardar gráficos con un control preciso sobre el formato de salida y la apariencia.
