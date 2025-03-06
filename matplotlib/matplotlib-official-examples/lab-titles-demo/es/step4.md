# Posicionamiento Avanzado de Títulos con Subgráficos

En este paso, aprenderás técnicas avanzadas para el posicionamiento de títulos cuando trabajes con diseños de subgráficos y objetos de ejes. También aprenderás cómo usar la función `suptitle()` para agregar un título general a una figura con múltiples subgráficos.

## Creación de una Figura con Subgráficos y Títulos Individuales

Vamos a crear una cuadrícula de subgráficos de 2x2, cada uno con su propio título posicionado de manera diferente:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

Ejecuta la celda. Deberías ver cuatro subgráficos, cada uno con un título posicionado de manera diferente.

## Agregar un Título a Nivel de Figura con suptitle()

Cuando trabajas con múltiples subgráficos, es posible que desees agregar un título general para toda la figura. Esto se puede hacer utilizando la función `suptitle()`:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Ejecuta la celda. Deberías ver cuatro subgráficos, cada uno con su propio título, y un título general para la figura en la parte superior.

## Combinación de Títulos de Ejes y Títulos de Figura

Puedes combinar títulos individuales de subgráficos con un título general de figura:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Ejecuta la celda. Deberías ver una figura con cuatro subgráficos, cada uno con un título posicionado de manera diferente, y un título general en la parte superior de la figura.

La función `suptitle()` es útil para agregar un título principal que describa toda la figura, mientras que las llamadas individuales a `set_title()` en objetos de ejes agregan títulos más específicos a cada subgráfico.
