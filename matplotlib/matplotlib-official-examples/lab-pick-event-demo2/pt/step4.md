# Adicionar Interatividade

Quando um ponto no gráfico de dispersão for clicado, queremos plotar os dados brutos (raw data) do conjunto de dados que gerou aquele ponto. Definiremos uma função `onpick` que será chamada quando um ponto for clicado. A função plotará os dados brutos e exibirá a média e o desvio padrão para aquele conjunto de dados.

```python
def onpick(event):

    if event.artist != line:
        return

    N = len(event.ind)
    if not N:
        return

    figi, axs = plt.subplots(N, squeeze=False)
    for ax, dataind in zip(axs.flat, event.ind):
        ax.plot(X[dataind])
        ax.text(.05, .9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    figi.show()


fig.canvas.mpl_connect('pick_event', onpick)
```
