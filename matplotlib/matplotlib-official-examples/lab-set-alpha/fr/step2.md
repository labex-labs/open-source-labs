# Création d'un diagramme à barres avec une valeur alpha uniforme

Dans cette étape, nous allons créer un diagramme à barres où toutes les barres ont le même niveau de transparence en utilisant l'argument mot-clé `alpha`.

## Ajout d'une nouvelle cellule

Ajoutez une nouvelle cellule à votre notebook Jupyter en cliquant sur le bouton "+" dans la barre d'outils ou en appuyant sur "Esc" puis sur "b" en mode commande.

## Création du diagramme à barres avec une valeur alpha uniforme

Entrez et exécutez le code suivant dans la nouvelle cellule :

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Comprendre le code et la sortie

Après avoir exécuté le code, vous devriez voir un diagramme à barres avec 20 barres. Chaque barre est soit verte (valeur positive de y) soit rouge (valeur négative de y) avec le même niveau de transparence (alpha = 0,5).

Décortiquons les parties clés :

1. `np.random.seed(19680801)` - Cela garantit que les nombres aléatoires générés sont les mêmes chaque fois que vous exécutez le code.

2. `x_values = list(range(20))` - Crée une liste d'entiers de 0 à 19 pour l'axe des x.

3. `y_values = np.random.randn(20)` - Génère 20 valeurs aléatoires à partir d'une distribution normale standard pour l'axe des y.

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - Cette compréhension de liste attribue la couleur verte aux valeurs positives et la couleur rouge aux valeurs négatives.

5. `ax.bar(..., alpha=0.5)` - La partie clé qui définit une valeur alpha uniforme de 0,5 pour toutes les barres.

La valeur alpha uniforme rend toutes les barres également transparentes, ce qui peut être utile lorsque vous souhaitez :

- Afficher les lignes de grille de fond à travers les barres
- Créer une visualisation plus subtile
- Réduire l'importance visuelle de tous les éléments de manière égale

Dans l'étape suivante, nous allons explorer comment définir des valeurs alpha différentes pour différentes barres.
