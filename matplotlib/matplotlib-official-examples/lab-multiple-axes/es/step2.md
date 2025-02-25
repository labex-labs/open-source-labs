# Crear la figura y los subtramas

El segundo paso es crear la figura y los subtramas que se utilizarán para la animación. En este ejemplo, creamos dos subtramas lado a lado con diferentes relaciones de aspecto. La subtrama izquierda es un círculo unitario y la subtrama derecha es una trama vacía que se utilizará para animar una curva senoidal.

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
