# Créer une figure et des sous-graphiques

Dans cette étape, nous allons créer une figure et quatre sous-graphiques pour chacune des projections que nous allons créer. Nous utiliserons la méthode `plt.subplots()` pour créer une figure et des sous-graphiques.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
