# Definindo a Função de Exemplo do Ciclo de Cores

Definimos a função `color_cycle_example` que recebe um objeto de eixo (axis object) como entrada e plota uma onda senoidal para cada cor no ciclo de cores. O ciclo de cores é definido pelos `rcParams`.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
