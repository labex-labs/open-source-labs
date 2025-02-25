# Créer une figure et un axe

Nous créons un objet figure avec `plt.figure()` et ajoutons un objet axe à l'aide de `fig1.add_axes()`. Nous définissons également la taille et la position de l'axe à l'aide de `[0,1, 0,1, 0,8, 0,8]`.

```python
fig1 = plt.figure()
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
```
