# Création d'une visualisation combinée avec différentes techniques d'alpha

Dans cette étape finale, nous allons combiner plusieurs techniques pour créer une visualisation plus complexe qui démontre à la fois des valeurs alpha uniformes et variables dans un seul graphique.

## Ajout d'une nouvelle cellule

Ajoutez une nouvelle cellule à votre notebook Jupyter en cliquant sur le bouton "+" dans la barre d'outils ou en appuyant sur "Esc" puis sur "b" en mode commande.

## Création d'une visualisation combinée

Entrez et exécutez le code suivant dans la nouvelle cellule :

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## Comprendre le code et la sortie

Après avoir exécuté le code, vous devriez voir une figure avec deux sous - graphiques côte à côte :

1. **Sous - graphique de gauche (Alpha uniforme)** : Affiche trois fonctions trigonométriques tracées avec la même valeur alpha (0,7).

2. **Sous - graphique de droite (Alpha variable)** : Affiche un nuage de points où :
   - L'abscisse est la valeur d'entrée.
   - L'ordonnée est sin(x)cos(x).
   - La taille de chaque point varie en fonction de la valeur absolue de l'ordonnée.
   - La couleur de chaque point varie en fonction de la valeur de l'ordonnée.
   - L'alpha (transparence) de chaque point varie en fonction de la valeur absolue de l'ordonnée.

Analysons les parties clés du code :

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - Crée une figure avec deux sous - graphiques côte à côte.

2. Pour le premier sous - graphique :
   - `ax1.plot(..., alpha=0.7)` - Utilise une valeur alpha uniforme pour les trois lignes.

3. Pour le deuxième sous - graphique :
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - Calcule des valeurs alpha variables entre 0,3 et 1,0.
   - `ax2.scatter(..., alpha=alphas)` - Utilise des valeurs alpha variables pour les points du nuage de points.

Cette combinaison de techniques démontre comment les valeurs alpha peuvent être utilisées de diverses manières pour améliorer les visualisations :

- **Alpha uniforme** est utile lorsque vous devez afficher plusieurs éléments qui se chevauchent avec une importance égale.

- **Alpha variable** est utile lorsque vous voulez mettre en évidence certains points de données en fonction de leurs valeurs.

En maîtrisant ces techniques, vous pouvez créer des visualisations de données plus efficaces et esthétiquement agréables.
