# Escribir una fórmula de LaTeX en el piso

Escribiremos una fórmula de LaTeX en el piso 'z = 0' del gráfico tridimensional utilizando la función `text3d`.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
