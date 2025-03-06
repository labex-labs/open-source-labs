# Erstellen einer wiederverwendbaren Funktion für Bildüberlagerungen

Um unseren Code wiederverwendbarer zu machen, erstellen wir eine Funktion, die ein Bild als Überlagerung zu jeder Matplotlib-Abbildung hinzufügen kann. So können wir denselben Effekt einfach auf verschiedene Diagramme anwenden.

1. Erstellen Sie eine neue Zelle in Ihrem Notebook und geben Sie den folgenden Code ein:

```python
def add_image_overlay(fig, image_path, x_pos=25, y_pos=25, alpha=0.5, zorder=3):
    """
    Add an image overlay to a matplotlib figure.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to add the image to
    image_path : str
        Path to the image file
    x_pos : int
        X position in pixels from the bottom left
    y_pos : int
        Y position in pixels from the bottom left
    alpha : float
        Transparency level (0 to 1)
    zorder : int
        Drawing order (higher numbers are drawn on top)

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure with the image overlay
    """
    # Load the image
    with cbook.get_sample_data(image_path) as file:
        im = image.imread(file)

    # Add the image to the figure
    fig.figimage(im, x_pos, y_pos, zorder=zorder, alpha=alpha)

    return fig

# Example usage: Create a scatter plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data for a scatter plot
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create a scatter plot
ax.scatter(x, y, s=100, c=np.random.rand(50), cmap='viridis', alpha=0.7)
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Scatter Plot with Image Overlay')

# Add the image overlay using our function
add_image_overlay(fig, 'logo2.png', x_pos=50, y_pos=50, alpha=0.4)

# Display the plot
plt.tight_layout()
plt.show()
```

Dieser Code definiert eine Funktion namens `add_image_overlay`, die:

- Parameter für die Abbildung, den Bildpfad, die Position, die Transparenz und die Zeichnungsreihenfolge (z-order) akzeptiert.
- Das angegebene Bild lädt.
- Das Bild mithilfe von `figimage` zur Abbildung hinzufügt.
- Die modifizierte Abbildung zurückgibt.

Nachdem die Funktion definiert wurde, demonstrieren wir ihre Verwendung, indem wir ein Streudiagramm mit Zufallsdaten erstellen und das Matplotlib-Logo als Überlagerung hinzufügen.

2. Führen Sie die Zelle aus, indem Sie Shift+Enter drücken.

Die Ausgabe sollte ein Streudiagramm mit zufällig positionierten und farbigen Punkten zeigen, sowie das Matplotlib-Logo, das an Position (50, 50) mit 40 % Opazität überlagert ist.

3. Versuchen wir noch ein Beispiel mit einem Linien Diagramm. Erstellen Sie eine neue Zelle und geben Sie den folgenden Code ein:

```python
# Example usage: Create a line plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data for a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
ax.plot(x, y, linewidth=2, color='#d62728')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Sine Wave with Image Overlay')
ax.set_ylim(-1.5, 1.5)

# Add the image overlay using our function
# Place it in the bottom right corner
fig_width, fig_height = fig.get_size_inches() * fig.dpi
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
    x_pos = fig_width - im.shape[1] - 50  # 50 pixels from the right edge

add_image_overlay(fig, 'logo2.png', x_pos=x_pos, y_pos=50, alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
```

Dieser Code erstellt ein Linien Diagramm, das eine Sinuswelle zeigt, und fügt das Matplotlib-Logo in die untere rechte Ecke des Diagramms ein.

4. Führen Sie die Zelle aus, indem Sie Shift+Enter drücken.

Die Ausgabe sollte ein Linien Diagramm einer Sinuswelle zeigen, mit dem Matplotlib-Logo, das in der unteren rechten Ecke mit 60 % Opazität überlagert ist.

Diese Beispiele zeigen, wie unsere `add_image_overlay`-Funktion verwendet werden kann, um einfach Bildüberlagerungen zu verschiedenen Diagrammtypen hinzuzufügen, was sie zu einem vielseitigen Werkzeug zur Anpassung von Visualisierungen macht.
