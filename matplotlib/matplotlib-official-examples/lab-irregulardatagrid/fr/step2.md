# Générez des données aléatoires

Nous générons des données aléatoires en utilisant la méthode `np.random.uniform` de NumPy. Nous générons `npts = 200` points de données avec des valeurs de x et y comprises entre -2 et 2. Nous calculons également les valeurs de z en utilisant la fonction `z = x * np.exp(-x**2 - y**2)`.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
