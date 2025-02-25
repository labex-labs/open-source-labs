# Ajouter du texte multiligne au deuxième sous-graphique

Dans le deuxième sous-graphique, nous allons ajouter du texte multiligne à l'aide de la fonction `text`. Nous pouvons spécifier la position, la taille, l'alignement vertical et horizontal, et la boîte englobante (bbox) du texte.

```python
ax1.text(0.29, 0.4, "Mat\nTTp\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.34, 0.4, "Mag\nTTT\n123", size=18,
         va="baseline", ha="left", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.95, 0.4, "Mag\nTTT$^{A^A}$\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))
```
