# Personnaliser les graphiques en barres

Nous allons maintenant personnaliser les graphiques en barres. Nous allons créer un tableau de couleurs et utiliser la méthode `bar()` pour tracer les graphiques en barres. Nous allons définir le paramètre `zdir` sur 'y' pour projeter les graphiques en barres sur les plans de l'axe y. Nous allons également définir le paramètre `alpha` sur 0,8 pour ajuster la transparence des barres.

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```
