# Génération des données

Ensuite, nous allons générer des données factices pour les utiliser dans notre graphique. Nous allons créer deux tableaux, `a` et `b`, à l'aide de la fonction `arange` de NumPy. Nous calculons ensuite deux tableaux supplémentaires, `c` et `d`, en utilisant la fonction `exp` pour calculer l'exponentielle de `a` et `d` comme l'inverse de `c`.

```python
# Make some fake data.
a = b = np.arange(0, 3,.02)
c = np.exp(a)
d = c[::-1]
```
