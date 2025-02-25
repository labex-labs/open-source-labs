# Créer des sous-graphiques pour les graphiques d'exemple

Nous allons créer une grille de sous-graphiques 3 x 3 pour afficher nos graphiques d'exemple.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
