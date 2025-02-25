# Creando un gráfico en estilo xkcd

En este paso, crearemos un gráfico en estilo xkcd que muestre la relación entre el tiempo y la salud general. El gráfico se basa en el cómic "Propiedad de una estufa" de XKCD.

```python
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    ax.annotate(
        'EL DÍA EN QUE ME DI CUENTA\nDE QUE PODÍA COCINAR BACON\nSIEMPRE QUE QUISIERA',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    ax.plot(data)

    ax.set_xlabel('tiempo')
    ax.set_ylabel('mi salud general')
    fig.text(
        0.5, 0.05,
        '"Propiedad de una estufa" de xkcd de Randall Munroe',
        ha='center')

plt.show()
```
