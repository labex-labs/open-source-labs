# Créer des sous-graphiques

Nous allons créer une grille de sous-graphiques 2x3 à l'aide de la fonction `subplots()`.

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
