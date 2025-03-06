# Création d'un nuage de points avec des valeurs alpha

Dans cette étape, nous allons appliquer nos connaissances sur les valeurs alpha pour créer un nuage de points. Cela démontrera comment la transparence peut aider à visualiser la densité des données dans les nuages de points avec des points qui se chevauchent.

## Ajout d'une nouvelle cellule

Ajoutez une nouvelle cellule à votre notebook Jupyter en cliquant sur le bouton "+" dans la barre d'outils ou en appuyant sur "Esc" puis sur "b" en mode commande.

## Création d'un nuage de points avec transparence

Entrez et exécutez le code suivant dans la nouvelle cellule :

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Comprendre le code et la sortie

Après avoir exécuté le code, vous devriez voir un nuage de points avec deux groupes de points. Chaque point a un niveau de transparence de 0,5, ce qui vous permet de voir où les points se chevauchent.

Décortiquons les parties clés du code :

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - Génère 500 coordonnées x aléatoires suivant une distribution normale de moyenne 0,3 et d'écart - type 0,15.

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - Génère 500 coordonnées y aléatoires pour le premier groupe.

3. `cluster2_x` et `cluster2_y` - Génèrent de manière similaire les coordonnées pour le deuxième groupe centré en (0,7 ; 0,7).

4. `ax.scatter(..., alpha=0.5)` - Crée un nuage de points avec des points à 50 % d'opacité.

Les avantages de l'utilisation de l'alpha dans les nuages de points incluent :

1. **Visualisation de la densité** : Les zones où de nombreux points se chevauchent apparaissent plus sombres, révélant la densité des données.

2. **Réduction du chevauchement des points** : Sans transparence, les points qui se chevauchent cacheraient complètement les uns les autres.

3. **Reconnaissance de motifs** : La transparence aide à identifier les groupes et les motifs dans les données.

Remarquez comment les zones avec plus de points qui se chevauchent apparaissent plus sombres dans la visualisation. C'est un moyen puissant de visualiser la densité des données sans avoir besoin de techniques supplémentaires comme l'estimation de densité.
