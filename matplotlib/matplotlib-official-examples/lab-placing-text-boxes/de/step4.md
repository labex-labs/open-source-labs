# Anpassen der Textbox

Nachdem wir erfolgreich eine Textbox zu unserem Diagramm hinzugefügt haben, lassen Sie uns verschiedene Anpassungsmöglichkeiten erkunden, um sie visuell ansprechender zu gestalten und für verschiedene Kontexte geeignet zu machen.

## Experimentieren mit verschiedenen Stilen

Wir erstellen eine Funktion, um es einfacher zu machen, mit verschiedenen Textbox-Stilen zu experimentieren. Geben Sie in einer neuen Zelle den folgenden Code ein und führen Sie ihn aus:

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

Jetzt verwenden wir diese Funktion, um verschiedene Box-Stile zu testen. Geben Sie in einer neuen Zelle ein und führen Sie aus:

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

Wenn Sie diese Zelle ausführen, sehen Sie vier verschiedene Diagramme, jedes mit einem anderen Textbox-Stil.

## Ändern der Textbox-Position

Die Position einer Textbox kann für die Visualisierung von entscheidender Bedeutung sein. Wir platzieren Textboxen in verschiedenen Ecken des Diagramms. Geben Sie in einer neuen Zelle ein und führen Sie aus:

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

Dieser Code erstellt ein 2x2-Raster von Histogrammen, jedes mit einer Textbox in einer anderen Ecke.

## Verständnis der Textbox-Positionierung

Es gibt mehrere Schlüsselparameter, die die Textbox-Positionierung steuern:

1. **Positions-Koordinaten**: Die `(x, y)`-Koordinaten bestimmen, wo die Textbox platziert wird. Wenn `transform=ax.transAxes` verwendet wird, sind dies Achsen-Koordinaten, wobei `(0, 0)` die untere linke Ecke und `(1, 1)` die obere rechte Ecke ist.

2. **Vertikale Ausrichtung**: Der Parameter `verticalalignment` steuert, wie der Text vertikal relativ zur y-Koordinate ausgerichtet wird:

   - `'top'`: Die Oberkante des Texts befindet sich an der angegebenen y-Koordinate.
   - `'center'`: Die Mitte des Texts befindet sich an der angegebenen y-Koordinate.
   - `'bottom'`: Die Unterkante des Texts befindet sich an der angegebenen y-Koordinate.

3. **Horizontale Ausrichtung**: Der Parameter `horizontalalignment` steuert, wie der Text horizontal relativ zur x-Koordinate ausgerichtet wird:
   - `'left'`: Die linke Kante des Texts befindet sich an der angegebenen x-Koordinate.
   - `'center'`: Die Mitte des Texts befindet sich an der angegebenen x-Koordinate.
   - `'right'`: Die rechte Kante des Texts befindet sich an der angegebenen x-Koordinate.

Diese Ausrichtungsoptionen sind besonders wichtig, wenn Text in Ecken platziert wird. Beispielsweise würden Sie in der oberen rechten Ecke `horizontalalignment='right'` verwenden, damit die rechte Kante des Texts mit der rechten Kante des Diagramms übereinstimmt.
