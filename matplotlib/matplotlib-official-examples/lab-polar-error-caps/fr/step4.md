# Création des barre d'erreur

Dans cette étape, nous allons créer des barre d'erreur sur notre axe polaire. Nous utiliserons la fonction `errorbar()` pour créer à la fois des barre d'erreur pour le rayon et pour theta.

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
