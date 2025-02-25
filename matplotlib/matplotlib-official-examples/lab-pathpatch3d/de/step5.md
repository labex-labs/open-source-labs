# Schreiben einer Latex-Formel auf dem Boden

Wir werden eine Latex-Formel auf dem z=0-'Boden' des 3D-Diagramms mit der `text3d`-Funktion schreiben.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
