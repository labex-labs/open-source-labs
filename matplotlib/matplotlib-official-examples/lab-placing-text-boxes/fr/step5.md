# Création d'une visualisation finale avec plusieurs éléments textuels

Dans cette étape finale, nous allons combiner tout ce que nous avons appris pour créer une visualisation complète qui inclut plusieurs éléments textuels de styles différents. Cela démontrera comment les boîtes de texte peuvent être utilisées pour améliorer la narration des données.

## Création d'une visualisation avancée

Créons un graphique plus sophistiqué qui inclut à la fois notre histogramme et quelques éléments visuels supplémentaires. Dans une nouvelle cellule, entrez et exécutez le code suivant :

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

Lorsque vous exécutez cette cellule, vous verrez une visualisation complète avec :

- Un histogramme des données avec un style amélioré
- Des lignes verticales marquant la moyenne et l'étendue d'un écart - type
- Une boîte de texte de statistiques dans le coin supérieur gauche
- Une boîte de texte informative sur les distributions normales dans le coin supérieur droit
- Une légende expliquant les lignes verticales

## Compréhension des éléments avancés

Examinons certains des nouveaux éléments que nous avons ajoutés :

1. **Lignes verticales avec `axvline()`** :

   - Ces lignes marquent directement sur le graphique des statistiques importantes.
   - Le paramètre `label` permet d'inclure ces lignes dans la légende.

2. **Plusieurs boîtes de texte de styles différents** :

   - Chaque boîte de texte a un objectif différent et utilise un style distinct.
   - La boîte de statistiques montre les valeurs calculées à partir de nos données.
   - La boîte informative fournit des informations contextuelles sur les distributions normales.

3. **Mise en forme améliorée** :

   - La mise en forme LaTeX est utilisée pour créer du texte en gras avec `\mathbf{}`
   - Des points de liste sont créés avec `\bullet`
   - L'espacement est contrôlé avec `\ ` (antislash suivi d'un espace)

4. **Grille et légende** :
   - La grille aide les spectateurs à lire plus précisément les valeurs du graphique.
   - La légende explique la signification des lignes colorées.

## Remarques finales sur le placement des boîtes de texte

Lorsque vous placez plusieurs éléments textuels dans une visualisation, considérez :

1. **Hiérarchie visuelle** : L'information la plus importante devrait ressortir le plus.
2. **Positionnement** : Placez les informations connexes près des parties pertinentes de la visualisation.
3. **Contraste** : Assurez - vous que le texte est lisible par rapport à son arrière - plan.
4. **Cohérence** : Utilisez un style cohérent pour les types d'informations similaires.
5. **Encombrement** : Évitez de surcharger la visualisation avec trop d'éléments textuels.

En plaçant et en stylisant judicieusement les boîtes de texte, vous pouvez créer des visualisations à la fois informatives et esthétiquement agréables, guidant les spectateurs pour qu'ils comprennent les informations clés de vos données.
