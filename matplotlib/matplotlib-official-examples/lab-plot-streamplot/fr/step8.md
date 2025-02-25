# Lignes de courant continues

Dans cette étape, nous allons créer un graphique de champ de flux avec des lignes de courant continues. Le paramètre `broken_streamlines` contrôle si les lignes de courant doivent être interrompues lorsqu'elles dépassent la limite de lignes dans une seule cellule de grille.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
