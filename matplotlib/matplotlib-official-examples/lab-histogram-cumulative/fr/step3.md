# Créez la figure et les sous-graphiques

Dans cette étape, nous allons créer une figure avec deux sous-graphiques pour les distributions cumulatives. Nous allons également définir la taille de la figure sur 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
