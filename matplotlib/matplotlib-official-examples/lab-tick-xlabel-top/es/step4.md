# Personalizar aún más el gráfico

Ahora que hemos movido las etiquetas de las marcas del eje x a la parte superior, personalicemos aún más nuestro gráfico para que sea más atractivo visualmente e informativo.

## Técnicas avanzadas de personalización de gráficos

Matplotlib ofrece numerosas opciones para personalizar gráficos. Exploremos algunas de estas opciones:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate some data with more points for a smoother curve
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple datasets
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Fill the area between curves
ax.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='green', interpolate=True)
ax.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='purple', interpolate=True)

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

# Add title and labels with custom styles
ax.set_title('Sine and Cosine Functions with Customized X-Axis Labels at the Top',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Function Value', fontsize=12)

# Add a grid and customize its appearance
ax.grid(True, linestyle='--', alpha=0.7, which='both')

# Customize the axis limits
ax.set_ylim(-1.2, 1.2)

# Add a legend with custom location and style
ax.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Add annotations to highlight important points
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, ha='center')

# Display the plot
plt.tight_layout()  # Adjust spacing for better appearance
plt.show()

print("We have created a fully customized plot with x-axis tick labels at the top!")
```

Cuando ejecutes este código, verás un gráfico mucho más elaborado y con aspecto profesional con:

- Dos curvas (seno y coseno)
- Regiones coloreadas entre las curvas
- Etiquetas de marcas personalizadas (utilizando notación de π)
- Anotaciones que señalan características clave
- Mejor espaciado y estilo

Observa cómo hemos mantenido las etiquetas de las marcas del eje x en la parte superior utilizando el método `tick_params()` pero hemos mejorado el gráfico con personalizaciones adicionales.

## Comprender las personalizaciones

Desglosemos algunas de las personalizaciones clave que hemos agregado:

1. `fill_between()`: Crea regiones coloreadas entre las curvas de seno y coseno.
2. `set_xticks()` y `set_xticklabels()`: Personalizan las posiciones y las etiquetas de las marcas.
3. `tight_layout()`: Ajusta automáticamente el espaciado del gráfico para una mejor apariencia.
4. `annotate()`: Agrega texto con una flecha que apunta a un punto específico.
5. Fuentes, colores y estilos personalizados para varios elementos.

Estas personalizaciones demuestran cómo se pueden crear gráficos visualmente atractivos e informativos mientras se mantienen las etiquetas de las marcas del eje x en la parte superior.
