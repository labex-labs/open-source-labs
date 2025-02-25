# Tracer la surface

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

Nous traçons la surface à l'aide de la fonction `plot_surface()`. Nous passons les valeurs de `X`, `Y` et `Z` ainsi que le paramètre `cmap` défini sur `cm.coolwarm` pour colorer la surface avec la carte de couleurs coolwarm. Nous définissons également `linewidth = 0` pour supprimer le maillage et `antialiased = False` pour rendre la surface opaque.
