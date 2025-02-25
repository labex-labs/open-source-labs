# Creando un gráfico de barras en estilo xkcd

En este paso, crearemos un gráfico de barras con el estilo xkcd. El gráfico se basa en el cómic "Los datos hasta ahora" de XKCD.

```python
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([0, 1], [0, 100], 0.25)
    ax.spines[['top', 'right']].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['CONFIRMADO POR\nEXPERIMENTO', 'REFUTADO POR\nEXPERIMENTO'])
    ax.set_xlim([-0.5, 1.5])
    ax.set_yticks([])
    ax.set_ylim([0, 110])

    ax.set_title("AFIRMACIONES DE PODERES SOBERNATURALES")

    fig.text(
        0.5, 0.05,
        '"Los datos hasta ahora" de xkcd de Randall Munroe',
        ha='center')

plt.show()
```
