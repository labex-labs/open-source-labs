# Définition de la fonction d'exemple de cycle de couleurs

Nous définissons la fonction `color_cycle_example` qui prend un objet d'axe en entrée et trace une onde sinusoïdale pour chaque couleur dans le cycle de couleurs. Le cycle de couleurs est défini par les `rcParams`.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
