# Définition de la fonction d'exemple d'image et de patch

Nous définissons la fonction `image_and_patch_example` qui prend un objet d'axe en entrée, trace une image aléatoire et ajoute un patch au tracé.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
