# Fixer la graine aléatoire et les bornes des bins

Fixez la graine aléatoire pour la reproductibilité et fixez les limites des bins.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```
