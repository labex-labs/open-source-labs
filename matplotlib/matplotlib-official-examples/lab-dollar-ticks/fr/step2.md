# Création d'un graphique financier de base

Maintenant que nos données sont prêtes, créons un graphique de base pour visualiser le chiffre d'affaires quotidien. Nous allons commencer par un simple graphique linéaire qui montre la tendance du chiffre d'affaires sur la période de 30 jours.

Dans une nouvelle cellule de votre notebook, ajoutez et exécutez le code suivant :

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Basic plot created successfully!")
```

Après avoir exécuté ce code, vous devriez voir un graphique linéaire montrant la tendance du chiffre d'affaires quotidien. Il devrait ressembler à ceci (les valeurs réelles peuvent varier légèrement en raison de la génération aléatoire) :

![Basic Revenue Plot](../assets/screenshot-20250306-ywFsL4VH@2x.png)

Analysons ce que nous avons fait dans ce code :

1. `fig, ax = plt.subplots(figsize=(10, 6))` - Nous avons créé une figure et des axes d'une taille de 10×6 pouces.
2. `ax.plot(days, daily_revenue, ...)` - Nous avons tracé nos données avec les jours sur l'axe des abscisses (x-axis) et le chiffre d'affaires sur l'axe des ordonnées (y-axis).
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - Nous avons ajouté des étiquettes et un titre à notre graphique.
4. `ax.grid()` - Nous avons ajouté une grille pour faciliter la lecture des données.
5. `plt.tight_layout()` - Nous avons ajusté le remplissage pour que tout s'adapte correctement.
6. `plt.show()` - Nous avons affiché le graphique.

Notez que l'axe des ordonnées affiche actuellement des nombres simples sans signes dollars. Dans l'étape suivante, nous allons modifier notre graphique pour afficher un formatage monétaire approprié sur l'axe des ordonnées.
