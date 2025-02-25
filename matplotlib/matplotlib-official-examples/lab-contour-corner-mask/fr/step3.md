# Masquage des données

Dans cette étape, nous allons masquer certaines des valeurs de `z` à l'aide d'un masque booléen. Nous créons un tableau `mask` à l'aide de la fonction `np.zeros_like()`, puis définissons certaines des valeurs sur `True` pour les masquer.

```python
# Masquer diverses valeurs de z.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
