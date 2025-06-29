# Ajout d'une boîte de texte avec des statistiques

Maintenant que nous avons un histogramme de base, améliorons - le en ajoutant une boîte de texte qui affiche les informations statistiques sur nos données. Cela rendra la visualisation plus informative pour les spectateurs.

## Création du contenu textuel

Tout d'abord, nous devons préparer le contenu textuel qui ira à l'intérieur de notre boîte de texte. Dans une nouvelle cellule, entrez et exécutez le code suivant :

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

Vous devriez voir une sortie similaire à :

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

Ce code crée une chaîne de caractères multi - ligne contenant la moyenne, la médiane et l'écart - type de nos données. Examinons quelques aspects intéressants de ce code :

1. La méthode `\n'.join(...)` joint plusieurs chaînes de caractères avec un caractère de nouvelle ligne entre elles.
2. Le `r` avant chaque chaîne de caractères la transforme en une chaîne "brute", ce qui est utile lorsqu'on inclut des caractères spéciaux.
3. La notation `$...$` est utilisée pour la mise en forme mathématique au style LaTeX dans matplotlib.
4. `\mu` et `\sigma` sont des symboles LaTeX pour les lettres grecques μ (mu) et σ (sigma).
5. `%.2f` est un spécificateur de format qui affiche un nombre à virgule flottante avec deux décimales.

## Création et ajout de la boîte de texte

Maintenant, recréons notre histogramme et ajoutons - lui la boîte de texte. Dans une nouvelle cellule, entrez et exécutez le code suivant :

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

Lorsque vous exécutez cette cellule, vous devriez voir votre histogramme avec une boîte de texte dans le coin supérieur gauche affichant les statistiques.

## Compréhension du code de la boîte de texte

Décortiquons les parties importantes du code qui créent la boîte de texte :

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)` :
   - Cela crée un dictionnaire avec les propriétés de la boîte de texte.
   - `boxstyle='round'` : Donne à la boîte des coins arrondis.
   - `facecolor='wheat'` : Définit la couleur de fond de la boîte en couleur blé.
   - `alpha=0.5` : Rend la boîte semi - transparente (opacité de 50 %).

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)` :
   - Cela ajoute du texte aux axes à la position (0,05, 0,95).
   - `transform=ax.transAxes` : C'est crucial - cela signifie que les coordonnées sont en unités d'axes (0 - 1) plutôt qu'en unités de données. Donc (0,05, 0,95) signifie "5 % depuis le bord gauche et 95 % depuis le bord inférieur du graphique".
   - `fontsize=14` : Définit la taille de la police.
   - `verticalalignment='top'` : Aligne le texte de sorte que le haut du texte soit à la coordonnée y spécifiée.
   - `bbox=properties` : Applique les propriétés de notre boîte de texte.

La boîte de texte restera à la même position par rapport aux axes du graphique, même si vous zoomez sur le graphique ou changez la plage de données. C'est parce que nous avons utilisé `transform=ax.transAxes`, qui utilise des coordonnées d'axes au lieu de coordonnées de données.
