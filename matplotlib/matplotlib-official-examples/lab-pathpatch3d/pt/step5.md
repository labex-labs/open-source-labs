# Escrever uma Fórmula Latex no Chão

Escrever-se-á uma fórmula Latex no 'chão' z=0 do gráfico 3D usando a função `text3d`.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
