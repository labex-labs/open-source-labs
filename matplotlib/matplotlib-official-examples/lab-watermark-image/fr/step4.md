# Superposition de l'image sur le graphique

Maintenant que nous avons créé notre graphique de base, superposons l'image dessus. Nous utiliserons la méthode `figimage` pour ajouter l'image à la figure, et nous la rendrons semi-transparente afin que le graphique en dessous reste visible.

1. Créez une nouvelle cellule dans votre notebook et entrez le code suivant :

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

Ce code combine ce que nous avons fait dans les étapes précédentes et ajoute la méthode `figimage` pour superposer notre image sur le graphique. Voici une explication des paramètres de `figimage` :

- `im` : Les données de l'image sous forme de tableau NumPy.
- `25, 25` : Les positions x et y en pixels à partir du coin inférieur gauche de la figure.
- `zorder=3` : Contrôle l'ordre de dessin. Les nombres plus élevés sont dessinés au-dessus des éléments avec des nombres plus bas.
- `alpha=0.5` : Contrôle la transparence de l'image. Une valeur de 0 est complètement transparente, et 1 est complètement opaque.

2. Exécutez la cellule en appuyant sur Shift+Enter.

La sortie devrait montrer le même diagramme à barres que précédemment, mais maintenant avec le logo de Matplotlib superposé dans le coin inférieur gauche. Le logo devrait être semi-transparent, permettant au graphique en dessous de rester visible.

3. Expérimentons avec différentes positions et niveaux de transparence. Créez une nouvelle cellule et entrez le code suivant :

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

Ce code place l'image au centre de la figure avec un niveau de transparence plus élevé (alpha = 0,3), la rendant plus adaptée comme filigrane.

4. Exécutez la cellule en appuyant sur Shift+Enter.

La sortie devrait montrer le diagramme à barres avec le logo centré et plus transparent que précédemment, créant un effet de filigrane.
