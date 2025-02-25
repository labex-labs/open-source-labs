# Création de sous-graphiques

Ensuite, nous créons les sous-graphiques à l'aide de `plt.subplot_mosaic`. Nous allons créer une grille 3x2 de sous-graphiques et les étiqueter comme suit :

- Le graphique en haut à gauche sera étiqueté "a)"
- Le graphique en bas à gauche sera étiqueté "b)"
- Les graphiques en haut à droite et en bas à droite seront étiquetés "c)" et "d)" respectivement.

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```
