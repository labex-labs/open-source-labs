# Определение функции примера цикла цветов

Мы определяем функцию `color_cycle_example`, которая принимает объект оси в качестве входных данных и строит синусоидальную волну для каждого цвета в цикле цветов. Цикл цветов определяется параметрами rcParams.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
