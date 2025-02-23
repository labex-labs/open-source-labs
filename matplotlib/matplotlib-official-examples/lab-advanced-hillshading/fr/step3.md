# Affichage de différentes variables à travers l'ombre et la couleur

Dans cette étape, vous allez apprendre à afficher différentes variables à travers l'ombre et la couleur.

```python
def shade_other_data():
    """Démontre l'affichage de différentes variables à travers l'ombre et la couleur."""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z1 = np.sin(x**2)  # Données pour l'ombre de relief
    z2 = np.cos(x**2 + y**2)  # Données pour la couleur

    norm = Normalize(z2.min(), z2.max())
    cmap = plt.cm.RdBu

    ls = LightSource(315, 45)
    rgb = ls.shade_rgb(cmap(norm(z2)), z1)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')
    ax.set_title('Ombre par une variable, couleur par une autre', size='x-large')
```
