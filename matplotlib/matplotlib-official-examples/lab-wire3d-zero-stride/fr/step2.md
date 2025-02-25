# Créer une figure et deux sous-graphiques

Nous allons créer une figure avec deux sous-graphiques en utilisant la méthode `subplots()`. Nous définirons également la projection sur `'3d'` de manière à ce que nos sous-graphiques soient tridimensionnels.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
