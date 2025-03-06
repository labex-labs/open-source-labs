# Mise en forme des étiquettes de l'axe des ordonnées (y-axis) avec des signes dollars

Maintenant que nous avons notre graphique de base, formattons les étiquettes de l'axe des ordonnées pour afficher des signes dollars. Cela rendra nos données financières plus lisibles et présentées de manière plus professionnelle.

Pour formater les étiquettes des graduations sur l'axe des ordonnées, nous allons utiliser le module `ticker` de Matplotlib, qui propose diverses options de formatage. Plus précisément, nous allons utiliser la classe `StrMethodFormatter` pour créer un formateur personnalisé pour notre axe des ordonnées.

Dans une nouvelle cellule de votre notebook, ajoutez et exécutez le code suivant :

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

Après avoir exécuté ce code, vous devriez voir un nouveau graphique avec des signes dollars sur les étiquettes de l'axe des ordonnées.

Expliquons la partie clé de ce code :

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

Voici ce que fait cette chaîne de formatage :

- `$` - Ajoute un signe dollar au début de chaque étiquette
- `{x:,.2f}` - Formate le nombre avec :
  - `,` - Une virgule comme séparateur de milliers (par exemple, 1 000 au lieu de 1000)
  - `.2f` - Deux décimales (par exemple, $1 234,56)

Ce formateur s'applique à toutes les étiquettes de graduation principales sur l'axe des ordonnées. Remarquez comment le graphique indique désormais clairement que les valeurs sont en dollars, ce qui le rend beaucoup plus adapté à la visualisation de données financières.
