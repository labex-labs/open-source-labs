# Posicionamiento Global de Títulos con RCParams

En este último paso, aprenderás cómo utilizar los parámetros de configuración en tiempo de ejecución (RCParams) de Matplotlib para establecer valores predeterminados globales para el posicionamiento de títulos. Esto es útil cuando deseas que todos los gráficos en tu cuaderno o script utilicen un posicionamiento de títulos consistente sin tener que especificarlo para cada gráfico individualmente.

## Comprensión de los RCParams en Matplotlib

El comportamiento de Matplotlib se puede personalizar utilizando una variable similar a un diccionario llamada `rcParams`. Esto te permite establecer valores predeterminados globales para varias propiedades, incluyendo el posicionamiento de títulos.

## Establecimiento del Posicionamiento Global de Títulos con rcParams

Vamos a establecer valores predeterminados globales para el posicionamiento de títulos y luego crear algunos gráficos que utilizarán automáticamente estas configuraciones:

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

Ejecuta la celda para ver los valores predeterminados. Ahora, vamos a modificar estas configuraciones:

```python
# Set new global defaults for title positioning
plt.rcParams['axes.titley'] = 1.05     # Set title y position higher
plt.rcParams['axes.titlepad'] = 10     # Set padding between title and plot
plt.rcParams['axes.titlelocation'] = 'left'  # Set default alignment to left

# Create a plot that will use the new defaults
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Global RCParams Settings')
plt.show()
```

Ejecuta la celda. Observa cómo el título se posiciona de acuerdo con las configuraciones globales que definimos, incluso aunque no especificamos ningún parámetro de posicionamiento en la función `title()`.

## Creación de Múltiples Gráficos con las Mismas Configuraciones

Vamos a crear varios gráficos que utilicen todas nuestras configuraciones globales:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot with titles that use global settings
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1} Using Global Settings')

plt.tight_layout()
plt.show()
```

Ejecuta la celda. Todos los títulos de los cuatro subgráficos deben estar posicionados de acuerdo con las configuraciones globales que definimos anteriormente.

## Restablecimiento de los RCParams a los Valores Predeterminados

Si deseas restablecer los RCParams a sus valores predeterminados, puedes utilizar la función `rcdefaults()`:

```python
# Reset to default settings
plt.rcdefaults()

# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Default Settings Again')
plt.show()
```

Ejecuta la celda. El título ahora debe estar posicionado utilizando las configuraciones predeterminadas de Matplotlib.

## Cambios Temporales de los RCParams

Si deseas cambiar temporalmente los RCParams solo para una sección específica de tu código, puedes utilizar un gestor de contexto:

```python
# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Default Settings')
plt.show()

# Temporarily change RCParams for just this section
with plt.rc_context({'axes.titlelocation': 'right', 'axes.titley': 1.1}):
    plt.figure(figsize=(8, 5))
    plt.plot(range(10))
    plt.grid(True)
    plt.title('Temporary Settings Change')
    plt.show()

# Create another plot that will use default settings again
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Back to Default Settings')
plt.show()
```

Ejecuta la celda. Deberías ver tres gráficos:

1. El primero con el posicionamiento de título predeterminado.
2. El segundo con el título alineado a la derecha y posicionado más alto (debido a las configuraciones temporales).
3. El tercero con el posicionamiento de título predeterminado nuevamente (ya que las configuraciones temporales solo se aplicaron dentro del gestor de contexto).

Este enfoque te permite realizar cambios temporales en las configuraciones globales sin afectar el resto de tus gráficos.
