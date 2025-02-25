# Écrire une formule LaTeX sur le sol

Nous allons écrire une formule LaTeX sur le "sol" z = 0 du graphique 3D à l'aide de la fonction `text3d`.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
