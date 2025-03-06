# Comprendre les valeurs alpha dans Matplotlib

Dans cette première étape, nous allons créer un notebook Jupyter et apprendre à configurer une visualisation de base avec des valeurs alpha.

## Création de votre première cellule de notebook Jupyter

Dans cette cellule, nous allons importer les bibliothèques nécessaires et créer deux cercles qui se chevauchent avec différentes valeurs alpha pour démontrer la transparence.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

Une fois que vous avez entré ce code dans la cellule, exécutez-le en appuyant sur Shift+Enter ou en cliquant sur le bouton "Run" dans la barre d'outils.

## Comprendre la sortie

Vous devriez voir deux cercles qui se chevauchent :

- Le cercle bleu à gauche est complètement opaque (alpha = 1,0)
- Le cercle rouge à droite est semi-transparent (alpha = 0,5)

Remarquez comment vous pouvez voir le cercle bleu à travers le cercle rouge là où ils se chevauchent. C'est l'effet de la définition de la valeur alpha à 0,5 pour le cercle rouge.

Les valeurs alpha contrôlent la transparence dans les visualisations et peuvent être utiles lorsque :

- Vous affichez des points de données qui se chevauchent
- Vous mettez en évidence certains éléments
- Vous réduisez le bruit visuel dans les graphiques denses
- Vous créez des visualisations en couches

Passons à l'étape suivante pour explorer davantage les applications des valeurs alpha.
