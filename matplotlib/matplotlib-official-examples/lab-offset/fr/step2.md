# Création des données

Ensuite, nous créons les données que nous utiliserons dans notre tracé. Dans cet exemple, nous allons utiliser NumPy pour générer les données.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
