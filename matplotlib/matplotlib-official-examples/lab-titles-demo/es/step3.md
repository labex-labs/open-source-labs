# Posicionamiento Vertical Personalizado de Títulos

A veces, es posible que desees ajustar la posición vertical de tu título. En este paso, aprenderás cómo controlar manualmente la posición vertical (eje y) de los títulos de tus gráficos.

## Comprensión de la Posición en el Eje Y de los Títulos

La posición vertical de un título se puede ajustar utilizando el parámetro `y` en la función `title()`. El parámetro `y` acepta valores en coordenadas normalizadas, donde:

- `y = 1.0` (valor predeterminado) coloca el título en la parte superior del gráfico.
- `y > 1.0` coloca el título por encima de la parte superior del gráfico.
- `y < 1.0` coloca el título por debajo de la parte superior del gráfico, acercándolo al contenido del gráfico.

## Creación de un Gráfico con una Posición en el Eje Y Personalizada para el Título

Vamos a crear un gráfico con el título posicionado más alto que la posición predeterminada. En una nueva celda, escribe el siguiente código:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

Ejecuta la celda. Observa cómo el título ahora aparece ligeramente más alto por encima del gráfico en comparación con la posición predeterminada.

Ahora, vamos a crear un gráfico con el título posicionado más bajo que la posición predeterminada:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

Ejecuta la celda. El título ahora debería aparecer más cerca del contenido del gráfico.

## Comparación de Diferentes Posiciones en el Eje Y

Vamos a crear múltiples gráficos uno al lado del otro para comparar diferentes posiciones verticales de los títulos:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

Ejecuta la celda para ver las tres posiciones verticales una al lado de la otra. Esta comparación te ayuda a entender cómo el parámetro `y` afecta la posición vertical del título.

## Combinación del Posicionamiento Horizontal y Vertical

Puedes combinar el parámetro `loc` (para la alineación horizontal) con el parámetro `y` (para la posición vertical) para colocar tu título exactamente donde lo desees:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

Ejecuta la celda. El título ahora debería aparecer alineado con el borde derecho del gráfico y posicionado más alto que la posición predeterminada.
