# Création d'un histogramme de base

Maintenant que nous avons nos données, créons un histogramme pour visualiser sa distribution. Un histogramme divise les données en intervalles (plages) et montre la fréquence des points de données dans chaque intervalle.

## Création de l'histogramme

Dans une nouvelle cellule de votre Jupyter Notebook, entrez et exécutez le code suivant :

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

Lorsque vous exécutez cette cellule, vous devriez voir un histogramme affichant la distribution de vos données aléatoires. La sortie ressemblera à une courbe en cloche (distribution normale) centrée autour de zéro.

## Compréhension du code

Décortiquons ce que chaque ligne du code fait :

1. `fig, ax = plt.subplots(figsize=(10, 6))` : Crée un objet figure et un objet axes. Le paramètre `figsize` définit la taille du graphique en pouces (largeur, hauteur).

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')` : Crée un histogramme de nos données `x` avec 50 intervalles. Les intervalles sont colorés en bleu ciel avec des bordures noires.

3. `ax.set_title('Distribution of Random Data', fontsize=16)` : Ajoute un titre au graphique avec une taille de police de 16.

4. `ax.set_xlabel('Value', fontsize=12)` et `ax.set_ylabel('Frequency', fontsize=12)` : Ajoutent des étiquettes aux axes x et y avec une taille de police de 12.

5. `plt.tight_layout()` : Ajuste automatiquement le graphique pour qu'il s'adapte à la zone de la figure.

6. `plt.show()` : Affiche le graphique.

L'histogramme montre comment nos données sont distribuées. Étant donné que nous avons utilisé `np.random.randn()`, qui génère des données selon une distribution normale, l'histogramme a une forme en cloche centrée autour de 0. La hauteur de chaque barre représente le nombre de points de données qui tombent dans cette plage.
