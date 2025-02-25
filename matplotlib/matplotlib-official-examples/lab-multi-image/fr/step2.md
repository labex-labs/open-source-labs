# Générer des données et créer des sous-graphiques

Ensuite, nous allons générer des données pour nos images. Nous allons créer une grille 3x2 de sous-graphiques, chacun contenant un tableau aléatoire de valeurs.

```python
np.random.seed(19680801)
Nr = 3
Nc = 2

fig, axs = plt.subplots(Nr, Nc)
fig.suptitle('Multiple images')

images = []
for i in range(Nr):
    for j in range(Nc):
        # Générer des données avec une plage qui varie d'un graphique à l'autre.
        data = ((1 + i + j) / 10) * np.random.rand(10, 20)
        images.append(axs[i, j].imshow(data))
        axs[i, j].label_outer()
```
