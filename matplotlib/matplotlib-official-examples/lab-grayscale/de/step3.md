# Definieren der Funktion für das Farbzyklusbeispiel

Wir definieren die Funktion `color_cycle_example`, die ein Achsenobjekt als Eingabe nimmt und für jede Farbe im Farbzyklus eine Sinuswelle darstellt. Der Farbzyklus wird durch die rcParams definiert.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
