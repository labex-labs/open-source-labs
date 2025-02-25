# Agregar cadenas de prueba a la gráfica

Agregaremos cuatro cadenas de prueba a cada subgráfico, cada una con un estilo y una posición diferentes. Utilizaremos el método `text()` para agregar el texto a los subgráficos.

```python
test_strings = ["lg", r"$\frac{1}{2}\pi$", r"$p^{3^A}$", r"$p_{3_2}$"]
for ax, usetex in zip(axs, [False, True]):
    ax.axvline(0, color="r")
    for i, s in enumerate(test_strings):
        ax.axhline(i, color="r")
        ax.text(0., 3 - i, s,
                usetex=usetex,
                verticalalignment="baseline",
                size=50,
                bbox=dict(pad=0, ec="k", fc="none"))
```
