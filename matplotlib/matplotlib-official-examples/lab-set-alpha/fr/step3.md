# Création d'un diagramme à barres avec des valeurs alpha variables

Dans cette étape, nous allons utiliser le format de tuple `(matplotlib_color, alpha)` pour attribuer différents niveaux de transparence à chaque barre en fonction de sa valeur de données.

## Ajout d'une nouvelle cellule

Ajoutez une nouvelle cellule à votre notebook Jupyter en cliquant sur le bouton "+" dans la barre d'outils ou en appuyant sur "Esc" puis sur "b" en mode commande.

## Création du diagramme à barres avec des valeurs alpha variables

Entrez et exécutez le code suivant dans la nouvelle cellule :

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Comprendre le code et la sortie

Après avoir exécuté le code, vous devriez voir un diagramme à barres avec 20 barres. Chaque barre a un niveau de transparence proportionnel à la valeur absolue de son axe y - les barres plus hautes sont plus opaques, les barres plus courtes sont plus transparentes.

Décortiquons les parties clés du code :

1. `abs_y = [abs(y) for y in y_values]` - Cela crée une liste des valeurs absolues de toutes les valeurs de y.

2. `max_abs_y = max(abs_y)` - Trouve la valeur absolue maximale pour normaliser les données.

3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` - Calcule les valeurs alpha entre 0,2 et 1,0 en fonction des valeurs absolues normalisées de y.

4. `colors_with_alphas = list(zip(facecolors, face_alphas))` - Crée une liste de tuples (couleur, alpha) en associant chaque couleur à sa valeur alpha correspondante.

5. `ax.bar(..., color=colors_with_alphas, ...)` - Utilise les tuples (couleur, alpha) pour définir des valeurs alpha différentes pour chaque barre.

Cette approche d'utilisation de niveaux de transparence variables est efficace pour :

- Mettre en évidence les points de données les plus significatifs
- Mettre moins en évidence les points de données moins significatifs
- Créer une hiérarchie visuelle basée sur les valeurs de données
- Ajouter une dimension supplémentaire d'information à votre visualisation

Vous pouvez clairement voir comment les valeurs alpha variables créent un effet visuel où l'amplitude d'un point de données est mise en évidence à la fois par la hauteur de la barre et son opacité.
