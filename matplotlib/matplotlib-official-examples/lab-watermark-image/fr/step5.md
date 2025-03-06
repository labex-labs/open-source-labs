# Création d'une fonction réutilisable pour les superpositions d'images

Pour rendre notre code plus réutilisable, créons une fonction qui peut ajouter une superposition d'image à n'importe quelle figure Matplotlib. De cette façon, nous pouvons facilement appliquer le même effet à différents graphiques.

1. Créez une nouvelle cellule dans votre notebook et entrez le code suivant :

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

Ce code définit une fonction appelée `add_image_overlay` qui :

- Prend en paramètres la figure, le chemin de l'image, la position, la transparence et l'ordre de dessin (z-order).
- Charge l'image spécifiée.
- Ajoute l'image à la figure en utilisant `figimage`.
- Retourne la figure modifiée.

Après avoir défini la fonction, nous démontrons son utilisation en créant un nuage de points avec des données aléatoires et en ajoutant le logo de Matplotlib en superposition.

2. Exécutez la cellule en appuyant sur Shift+Enter.

La sortie devrait montrer un nuage de points avec des points positionnés et colorés aléatoirement, et le logo de Matplotlib superposé à la position (50, 50) avec une opacité de 40 %.

3. Essayons un autre exemple avec un graphique linéaire. Créez une nouvelle cellule et entrez le code suivant :

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

Ce code crée un graphique linéaire montrant une onde sinusoïdale et ajoute le logo de Matplotlib dans le coin inférieur droit du graphique.

4. Exécutez la cellule en appuyant sur Shift+Enter.

La sortie devrait montrer un graphique linéaire d'une onde sinusoïdale avec le logo de Matplotlib superposé dans le coin inférieur droit avec une opacité de 60 %.

Ces exemples démontrent comment notre fonction `add_image_overlay` peut être utilisée pour ajouter facilement des superpositions d'images à différents types de graphiques, en faisant d'elle un outil polyvalent pour personnaliser les visualisations.
