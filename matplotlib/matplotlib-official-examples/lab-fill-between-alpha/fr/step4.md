# Mise en évidence de plages d'un axe avec `axhspan` et `axvspan`

Un autre usage pratique des régions remplies est de mettre en évidence des plages horizontales ou verticales d'un axe. Pour cela, Matplotlib dispose des fonctions d'aide `axhspan` et `axvspan`. Consultez la galerie `axhspan_demo` pour plus d'informations.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
