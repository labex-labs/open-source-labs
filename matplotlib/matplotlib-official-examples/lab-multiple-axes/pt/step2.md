# Criar a Figura e os Subplots

O segundo passo é criar a figura e os subplots que serão usados para a animação. Neste exemplo, criamos dois subplots lado a lado com diferentes proporções de aspecto. O subplot da esquerda é um círculo unitário, e o subplot da direita é um gráfico vazio que será usado para animar uma curva senoidal.

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
