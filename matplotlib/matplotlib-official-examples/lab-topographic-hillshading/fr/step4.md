# Spécifier la source de lumière et la carte de couleurs

Nous spécifions l'objet LightSource en définissant l'azimut et l'altitude de la source de lumière. Nous définissons également la carte de couleurs à utiliser dans le tracé.

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
