# Formateo de las Etiquetas del Eje Y con Signos de Dólar

Ahora que tenemos nuestra gráfica básica, formateemos las etiquetas del eje y para mostrar signos de dólar. Esto hará que nuestros datos financieros sean más legibles y se presenten de manera más profesional.

Para formatear las etiquetas de las marcas (ticks) en el eje y, utilizaremos el módulo `ticker` de Matplotlib, que proporciona diversas opciones de formato. En concreto, usaremos la clase `StrMethodFormatter` para crear un formateador personalizado para nuestro eje y.

En una nueva celda de su cuaderno (notebook), agregue y ejecute el siguiente código:

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

Después de ejecutar este código, debería ver una nueva gráfica con signos de dólar en las etiquetas del eje y.

Expliquemos la parte clave de este código:

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

Esto es lo que hace esta cadena de formato:

- `$` - Agrega un signo de dólar al principio de cada etiqueta
- `{x:,.2f}` - Formatea el número con:
  - `,` - Una coma como separador de miles (por ejemplo, 1,000 en lugar de 1000)
  - `.2f` - Dos decimales (por ejemplo, $1,234.56)

Este formateador se aplica a todas las etiquetas de las marcas principales en el eje y. Note cómo la gráfica ahora indica claramente que los valores están en dólares, lo que la hace mucho más adecuada para la visualización de datos financieros.
