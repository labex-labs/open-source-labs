# Création d'un graphique et d'une image

Ensuite, nous allons créer un graphique et une image pour montrer comment ajouter une barre de couleur à l'aide d'axes insérés.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```
