# Définissez les valeurs de x, y et z

Nous allons générer les valeurs de x, y et z à l'aide de NumPy. Nous allons tout d'abord définir la plage de valeurs pour theta et z. Ensuite, nous utiliserons ces valeurs pour générer les valeurs de r, x et y.

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
