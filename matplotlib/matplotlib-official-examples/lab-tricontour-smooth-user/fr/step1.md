# Fonction de test analytique

Dans cette étape, nous définissons une fonction de test analytique qui sera utilisée pour générer des valeurs de z pour la triangulation. La fonction s'appelle `function_z` et prend deux arguments, `x` et `y`. Elle calcule `z` en fonction des valeurs de `x` et `y`, et renvoie les valeurs normalisées de `z`.

```python
def function_z(x, y):
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = -(2 * (np.exp((r1 / 10)**2) - 1) * 30. * np.cos(7. * theta1) +
          (np.exp((r2 / 10)**2) - 1) * 30. * np.cos(11. * theta2) +
          0.7 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```
