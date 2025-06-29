# Personalización de la caja de texto

Ahora que hemos agregado con éxito una caja de texto a nuestro gráfico, exploremos varias opciones de personalización para hacerla más atractiva visualmente y adecuada para diferentes contextos.

## Experimentar con diferentes estilos

Creemos una función para facilitar la experimentación con diferentes estilos de cajas de texto. En una nueva celda, ingrese y ejecute el siguiente código:

```python
def plot_with_textbox(boxstyle, facecolor, alpha, position=(0.05, 0.95)):
    """
    Create a histogram with a custom text box.

    Parameters:
    boxstyle (str): Style of the box ('round', 'square', 'round4', etc.)
    facecolor (str): Background color of the box
    alpha (float): Transparency of the box (0-1)
    position (tuple): Position of the box in axes coordinates (x, y)
    """
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title and labels
    ax.set_title(f'Text Box Style: {boxstyle}', fontsize=16)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    # Create text box properties
    box_props = dict(boxstyle=boxstyle, facecolor=facecolor, alpha=alpha)

    # Add text box
    ax.text(position[0], position[1], textstr, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=box_props)

    plt.tight_layout()
    plt.show()
```

Ahora, usemos esta función para probar diferentes estilos de cajas. En una nueva celda, ingrese y ejecute:

```python
# Try a square box with light green color
plot_with_textbox('square', 'lightgreen', 0.7)

# Try a rounded box with light blue color
plot_with_textbox('round', 'lightblue', 0.5)

# Try a box with extra rounded corners
plot_with_textbox('round4', 'lightyellow', 0.6)

# Try a sawtooth style box
plot_with_textbox('sawtooth', 'lightcoral', 0.4)
```

Cuando ejecute esta celda, verá cuatro gráficos diferentes, cada uno con un estilo de caja de texto diferente.

## Cambiar la posición de la caja de texto

La posición de una caja de texto puede ser crucial para la visualización. Coloquemos cajas de texto en diferentes esquinas del gráfico. En una nueva celda, ingrese y ejecute:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # Flatten to easily iterate

# Define positions for the four corners
positions = [
    (0.05, 0.95),  # Top left
    (0.95, 0.95),  # Top right
    (0.05, 0.05),  # Bottom left
    (0.95, 0.05)   # Bottom right
]

# Define alignments for each position
alignments = [
    ('top', 'left'),          # Top left
    ('top', 'right'),         # Top right
    ('bottom', 'left'),       # Bottom left
    ('bottom', 'right')       # Bottom right
]

# Corner labels
corner_labels = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

# Create four plots with text boxes in different corners
for i, ax in enumerate(axes):
    # Plot histogram
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title
    ax.set_title(f'Text Box in {corner_labels[i]}', fontsize=14)

    # Create text box properties
    box_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # Add text box
    ax.text(positions[i][0], positions[i][1], textstr,
            transform=ax.transAxes, fontsize=12,
            verticalalignment=alignments[i][0],
            horizontalalignment=alignments[i][1],
            bbox=box_props)

plt.tight_layout()
plt.show()
```

Este código crea una cuadrícula de 2x2 de histogramas, cada uno con una caja de texto en una esquina diferente.

## Comprender el posicionamiento de la caja de texto

Hay varios parámetros clave que controlan el posicionamiento de la caja de texto:

1. **Coordenadas de posición**: Las coordenadas `(x, y)` determinan dónde se coloca la caja de texto. Cuando se usa `transform=ax.transAxes`, estas están en coordenadas de ejes donde `(0, 0)` es la esquina inferior izquierda y `(1, 1)` es la esquina superior derecha.

2. **Alineación vertical**: El parámetro `verticalalignment` controla cómo se alinea el texto verticalmente en relación con la coordenada y:
   - `'top'`: La parte superior del texto está en la coordenada y especificada.
   - `'center'`: El centro del texto está en la coordenada y especificada.
   - `'bottom'`: La parte inferior del texto está en la coordenada y especificada.

3. **Alineación horizontal**: El parámetro `horizontalalignment` controla cómo se alinea el texto horizontalmente en relación con la coordenada x:
   - `'left'`: El borde izquierdo del texto está en la coordenada x especificada.
   - `'center'`: El centro del texto está en la coordenada x especificada.
   - `'right'`: El borde derecho del texto está en la coordenada x especificada.

Estas opciones de alineación son particularmente importantes cuando se coloca texto en las esquinas. Por ejemplo, en la esquina superior derecha, querría usar `horizontalalignment='right'` para que el borde derecho del texto se alinee con el borde derecho del gráfico.
