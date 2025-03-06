# Überlagern des Bildes auf dem Diagramm

Nachdem wir unser Basisdiagramm erstellt haben, überlagern wir nun das Bild darauf. Wir verwenden die Methode `figimage`, um das Bild der Abbildung hinzuzufügen, und machen es halbtransparent, damit das darunter liegende Diagramm weiterhin sichtbar bleibt.

1. Erstellen Sie eine neue Zelle in Ihrem Notebook und geben Sie den folgenden Code ein:

```python
# Create a figure and axes for our plot (same as before)
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

Dieser Code kombiniert das, was wir in den vorherigen Schritten getan haben, und fügt die `figimage`-Methode hinzu, um unser Bild auf dem Diagramm zu überlagern. Hier ist eine Aufschlüsselung der `figimage`-Parameter:

- `im`: Die Bilddaten als NumPy-Array.
- `25, 25`: Die x- und y-Positionen in Pixeln vom unteren linken Eck der Abbildung aus.
- `zorder=3`: Steuert die Zeichnungsreihenfolge. Höhere Zahlen werden über Elementen mit niedrigeren Zahlen gezeichnet.
- `alpha=0.5`: Steuert die Transparenz des Bildes. Ein Wert von 0 ist vollständig transparent, und 1 ist vollständig undurchsichtig.

2. Führen Sie die Zelle aus, indem Sie Shift+Enter drücken.

Die Ausgabe sollte dasselbe Balkendiagramm wie zuvor zeigen, aber nun mit dem Matplotlib-Logo, das in der unteren linken Ecke überlagert ist. Das Logo sollte halbtransparent sein, sodass das darunter liegende Diagramm weiterhin sichtbar bleibt.

3. Experimentieren wir mit verschiedenen Positionen und Transparenzgraden. Erstellen Sie eine neue Zelle und geben Sie den folgenden Code ein:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

Dieser Code platziert das Bild in der Mitte der Abbildung mit einem höheren Transparenzgrad (alpha = 0,3), wodurch es besser als Wasserzeichen geeignet ist.

4. Führen Sie die Zelle aus, indem Sie Shift+Enter drücken.

Die Ausgabe sollte das Balkendiagramm mit dem zentrierten und transparenteren Logo als zuvor zeigen, wodurch ein Wasserzeicheneffekt entsteht.
