# Defining the Color Cycle Example Function

We define the `color_cycle_example` function that takes an axis object as input and plots a sine wave for each color in the color cycle. The color cycle is defined by the rcParams.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
