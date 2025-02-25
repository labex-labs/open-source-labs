# Créer un graphique

Ensuite, nous allons créer un graphique en utilisant la fonction `imshow` de Matplotlib. Cette fonction affiche une image sur le graphique. Nous allons également créer une figure avec deux sous-graphiques.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
