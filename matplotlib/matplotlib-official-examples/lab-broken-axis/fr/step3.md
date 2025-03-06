# Ajout de touches finales au graphique à axe brisé

Dans cette étape finale, nous allons ajouter des touches finales à notre graphique à axe brisé pour indiquer clairement que l'axe des ordonnées (y-axis) est brisé. Nous allons ajouter des lignes diagonales entre les sous-graphiques pour indiquer la rupture, et nous allons améliorer l'apparence globale du graphique avec des étiquettes appropriées et une grille.

## Ajout de lignes diagonales de rupture

Pour indiquer visuellement que l'axe est brisé, nous allons ajouter des lignes diagonales entre les deux sous-graphiques. C'est une convention courante qui aide les spectateurs à comprendre qu'une partie de l'axe a été omise.

Créez une nouvelle cellule et ajoutez le code suivant :

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

Lorsque vous exécutez cette cellule, vous devriez voir le graphique à axe brisé complet avec des lignes diagonales indiquant la rupture de l'axe des ordonnées. Le graphique a maintenant un titre, des étiquettes d'axes et des lignes de grille pour améliorer la lisibilité.

## Compréhension du graphique à axe brisé

Prenons un moment pour comprendre les éléments clés de notre graphique à axe brisé :

1. **Deux sous-graphiques** : Nous avons créé deux sous-graphiques distincts, chacun se concentrant sur une plage différente de valeurs de l'axe des ordonnées.
2. **Bords masqués** : Nous avons masqué les bords de connexion entre les sous-graphiques pour créer une séparation visuelle.
3. **Lignes diagonales de rupture** : Nous avons ajouté des lignes diagonales pour indiquer que l'axe est brisé.
4. **Limites de l'axe des ordonnées** : Nous avons défini des limites différentes pour l'axe des ordonnées de chaque sous-graphique pour nous concentrer sur des parties spécifiques des données.
5. **Lignes de grille** : Nous avons ajouté des lignes de grille pour améliorer la lisibilité et faciliter l'estimation des valeurs.

Cette technique est particulièrement utile lorsque vous avez des valeurs aberrantes (outliers) dans vos données qui compresseraient autrement la visualisation de la majorité de vos points de données. En « brisant » l'axe, vous pouvez montrer clairement à la fois les valeurs aberrantes et la distribution principale des données dans une seule figure.

## Expérimentation avec le graphique

Maintenant que vous savez comment créer un graphique à axe brisé, vous pouvez expérimenter avec différentes configurations. Essayez de changer les limites de l'axe des ordonnées, d'ajouter plus de fonctionnalités au graphique ou d'appliquer cette technique à vos propres données.

Par exemple, vous pouvez modifier le code précédent pour inclure une légende, changer le schéma de couleurs ou ajuster les styles de marqueurs :

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes with different styles
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Mark the outliers with a different color
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the top subplot
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

Lorsque vous exécutez ce code amélioré, vous devriez voir une visualisation améliorée avec les valeurs aberrantes spécifiquement marquées et une légende expliquant les points de données.

Félicitations ! Vous avez réussi à créer un graphique à axe brisé en Python en utilisant Matplotlib. Cette technique vous aidera à créer des visualisations plus efficaces lorsque vous aurez à traiter des données contenant des valeurs aberrantes.
