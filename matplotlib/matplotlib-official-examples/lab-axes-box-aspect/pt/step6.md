# Aspecto da Caixa (Box Aspect) para Muitos Subplots

É possível passar o aspecto da caixa (box aspect) para um Axes na inicialização. O seguinte cria uma grade de subplot 2 por 3 com todos os Axes quadrados.

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
