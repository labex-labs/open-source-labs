# Personnalisation de la boîte de texte

Maintenant que nous avons réussi à ajouter une boîte de texte à notre graphique, explorons diverses options de personnalisation pour la rendre plus attrayante visuellement et adaptée à différents contextes.

## Expérimentation avec différents styles

Créons une fonction pour faciliter l'expérimentation avec différents styles de boîtes de texte. Dans une nouvelle cellule, entrez et exécutez le code suivant :

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

Maintenant, utilisons cette fonction pour tester différents styles de boîtes. Dans une nouvelle cellule, entrez et exécutez :

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

Lorsque vous exécutez cette cellule, vous verrez quatre graphiques différents, chacun avec un style de boîte de texte différent.

## Changement de la position de la boîte de texte

La position d'une boîte de texte peut être cruciale pour la visualisation. Plaçons des boîtes de texte dans différents coins du graphique. Dans une nouvelle cellule, entrez et exécutez :

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

Ce code crée une grille de 2x2 d'histogrammes, chacun avec une boîte de texte dans un coin différent.

## Compréhension du positionnement de la boîte de texte

Plusieurs paramètres clés contrôlent le positionnement de la boîte de texte :

1. **Coordonnées de position** : Les coordonnées `(x, y)` déterminent où la boîte de texte est placée. Lorsque vous utilisez `transform=ax.transAxes`, il s'agit de coordonnées d'axes où `(0, 0)` est le coin inférieur gauche et `(1, 1)` est le coin supérieur droit.

2. **Alignement vertical** : Le paramètre `verticalalignment` contrôle l'alignement vertical du texte par rapport à la coordonnée y :
   - `'top'` : Le haut du texte est à la coordonnée y spécifiée.
   - `'center'` : Le centre du texte est à la coordonnée y spécifiée.
   - `'bottom'` : Le bas du texte est à la coordonnée y spécifiée.

3. **Alignement horizontal** : Le paramètre `horizontalalignment` contrôle l'alignement horizontal du texte par rapport à la coordonnée x :
   - `'left'` : Le bord gauche du texte est à la coordonnée x spécifiée.
   - `'center'` : Le centre du texte est à la coordonnée x spécifiée.
   - `'right'` : Le bord droit du texte est à la coordonnée x spécifiée.

Ces options d'alignement sont particulièrement importantes lors du placement de texte dans les coins. Par exemple, dans le coin supérieur droit, vous voudrez utiliser `horizontalalignment='right'` pour que le bord droit du texte s'aligne avec le bord droit du graphique.
