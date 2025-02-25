# Créez le graphique en barres

Ensuite, nous créons le graphique en barres empilées. Nous commençons par définir les paramètres du graphique :

```python
# paramètres du graphique en barres
bas = 1
largeur =.2

# Ajouter depuis le haut correspond à la légende.
for j, (hauteur, étiquette) in enumerate(reversed([*zip(rapports_âge, étiquettes_âge)])):
    bas -= hauteur
    bc = ax2.bar(0, hauteur, largeur, bottom=bas, color='C0', label=étiquette,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{hauteur:.0%}"], label_type='center')
```
