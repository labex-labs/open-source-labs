# Création et configuration du graphique à axe brisé

Dans cette étape, nous allons créer la structure réelle du graphique à axe brisé. Un graphique à axe brisé se compose de plusieurs sous-graphiques qui affichent différentes plages de la même donnée. Nous allons configurer ces sous-graphiques pour afficher efficacement nos données principales et nos valeurs aberrantes (outliers).

## Création des sous-graphiques

Tout d'abord, nous devons créer deux sous-graphiques disposés verticalement. Le sous-graphique supérieur affichera nos valeurs aberrantes, tandis que le sous-graphique inférieur montrera la majorité de nos points de données.

Créez une nouvelle cellule dans votre notebook et ajoutez le code suivant :

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Add a main title to the figure
fig.suptitle('Broken Axis Plot Example', fontsize=16)

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Display the figure to see both subplots
plt.tight_layout()
plt.show()
```

![broken-axis-plot](../assets/screenshot-20250306-cawcMZv3@2x.png)

Lorsque vous exécutez cette cellule, vous devriez voir une figure avec deux sous-graphiques, tous deux affichant les mêmes données. Remarquez comment les valeurs aberrantes compressent le reste des données dans les deux graphiques, rendant difficile la visualisation des détails de la majorité des points de données. C'est exactement le problème que nous essayons de résoudre avec un graphique à axe brisé.

## Configuration des limites de l'axe des ordonnées (Y)

Maintenant, nous devons configurer chaque sous-graphique pour nous concentrer sur une plage spécifique de valeurs de l'axe des ordonnées. Le sous-graphique supérieur se concentrera sur la plage des valeurs aberrantes, tandis que le sous-graphique inférieur se concentrera sur la plage des données principales.

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

# Add a title to each subplot
ax1.set_title('Outlier Region')
ax2.set_title('Main Data Region')

# Display the figure with adjusted y-axis limits
plt.tight_layout()
plt.show()
```

Lorsque vous exécutez cette cellule, vous devriez voir que chaque sous-graphique se concentre maintenant sur une plage différente de valeurs de l'axe des ordonnées. Le graphique supérieur montre seulement les valeurs aberrantes, et le graphique inférieur montre seulement les données principales. Cela améliore déjà la visualisation, mais pour en faire un véritable graphique à axe brisé, nous devons ajouter quelques configurations supplémentaires.

## Masquage des bords (spines) et ajustement des graduations (ticks)

Pour créer l'illusion d'un axe « brisé », nous devons masquer les bords de connexion entre les deux sous-graphiques et ajuster la position des graduations.

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

# Add labels to the plot
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')

plt.tight_layout()
plt.show()
```

Lorsque vous exécutez cette cellule, vous devriez voir que le graphique a maintenant des bords masqués entre les deux sous-graphiques, donnant un aspect plus propre. Les graduations de l'axe des abscisses sont maintenant correctement positionnées, avec des étiquettes seulement en bas.

À ce stade, nous avons réussi à créer un graphique à axe brisé de base. Dans l'étape suivante, nous ajouterons des touches finales pour que les spectateurs comprennent clairement que l'axe est brisé.
