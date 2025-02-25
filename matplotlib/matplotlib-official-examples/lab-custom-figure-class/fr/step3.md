# Créez des données pour le tracé

Créez quelques données pour le tracé. Dans cet exemple, nous allons créer des tableaux `x` et `y` à l'aide de la bibliothèque `numpy`.

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```
