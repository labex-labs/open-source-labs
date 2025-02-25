# Créer le graphique

Maintenant que nous avons les données, nous pouvons créer le graphique. Tout d'abord, nous créons un objet figure et un objet axe à l'aide de `plt.subplots()`. Ensuite, nous traçons les données à l'aide de `ax.plot()`.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```
