# Éviter les valeurs aberrantes dans les graphiques ombrés

Dans cette étape, vous allez apprendre à utiliser une norm personnalisée pour contrôler la plage de valeurs de z affichées dans un graphique ombré.

```python
def avoid_outliers():
    """Utiliser une norm personnalisée pour contrôler la plage de valeurs de z affichées dans un graphique ombré."""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z = 10 * np.cos(x**2 + y**2)

    # Ajouter quelques valeurs aberrantes...
    z[100, 105] = 2000
    z[120, 110] = -9000

    ls = LightSource(315, 45)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4.5))

    rgb = ls.shade(z, plt.cm.copper)
    ax1.imshow(rgb, interpolation='bilinear')
    ax1.set_title('Plage complète des données')

    rgb = ls.shade(z, plt.cm.copper, vmin=-10, vmax=10)
    ax2.imshow(rgb, interpolation='bilinear')
    ax2.set_title('Plage définie manuellement')

    fig.suptitle('Éviter les valeurs aberrantes dans les graphiques ombrés', size='x-large')
```
