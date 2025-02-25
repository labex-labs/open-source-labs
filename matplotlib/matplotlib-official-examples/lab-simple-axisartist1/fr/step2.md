# Création d'une figure et de sous-graphiques

Nous allons créer une figure avec deux sous-graphiques en utilisant la méthode `add_gridspec`.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```
