# Création d'une barre de couleur

Nous allons créer une barre de couleur pour montrer la correspondance entre les couleurs et les valeurs de `dydx`. Nous utiliserons la fonction `colorbar` de `matplotlib.pyplot` pour créer une barre de couleur.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
