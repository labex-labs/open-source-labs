# Creación de una Gráfica Financiera Básica

Ahora que tenemos nuestros datos listos, creemos una gráfica básica para visualizar los ingresos diarios. Comenzaremos con una simple gráfica de línea que muestre la tendencia de los ingresos durante el período de 30 días.

En una nueva celda de su cuaderno (notebook), agregue y ejecute el siguiente código:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Basic plot created successfully!")
```

Después de ejecutar este código, debería ver una gráfica de línea que muestra la tendencia de los ingresos diarios. Debería verse algo así (los valores reales pueden variar ligeramente debido a la generación aleatoria):

![Basic Revenue Plot](../assets/screenshot-20250306-ywFsL4VH@2x.png)

Analicemos lo que hicimos en este código:

1. `fig, ax = plt.subplots(figsize=(10, 6))` - Creamos una figura y ejes con un tamaño de 10×6 pulgadas
2. `ax.plot(days, daily_revenue, ...)` - Graficamos nuestros datos con los días en el eje x y los ingresos en el eje y
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - Agregamos etiquetas y un título a nuestra gráfica
4. `ax.grid()` - Agregamos una cuadrícula para que los datos sean más fáciles de leer
5. `plt.tight_layout()` - Ajustamos el relleno para asegurarnos de que todo quede bien dispuesto
6. `plt.show()` - Mostramos la gráfica

Note que actualmente el eje y muestra números simples sin signos de dólar. En el siguiente paso, modificaremos nuestra gráfica para mostrar un formato de moneda adecuado en el eje y.
