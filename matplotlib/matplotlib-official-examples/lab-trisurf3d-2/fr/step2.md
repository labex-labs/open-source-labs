# Créer un maillage

Nous créons un maillage dans l'espace des variables de paramétrisation `u` et `v`. Cela est fait à l'aide de la fonction `np.meshgrid()` pour créer une grille de points `u` et `v`.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
