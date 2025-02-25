# Création des données

Nous devons créer les données que nous utiliserons pour créer le graphe de niveau. Dans cet exemple, nous allons créer deux fonctions gaussiennes 2D.

```python
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
