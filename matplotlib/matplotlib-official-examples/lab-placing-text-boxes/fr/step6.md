# Ajout de la boîte de texte au graphique

Enfin, nous allons ajouter la boîte de texte au graphique en utilisant `matplotlib.pyplot.text()`. Nous spécifierons l'emplacement de la boîte de texte en coordonnées d'axes et utiliserons le paramètre `bbox` pour ajouter les propriétés de la boîte.

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
