# Création d'une figure et de sous-graphiques

L'étape suivante est de créer une figure et des sous-graphiques. Nous allons créer une figure avec deux sous-graphiques côte à côte à l'aide de la fonction `subplots`.

```python
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
```
