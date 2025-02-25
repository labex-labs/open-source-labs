# Générer des données

Ensuite, nous devons générer des données à tracer. Dans cet exemple, nous allons créer trois tableaux : un pour les valeurs de l'axe x, un pour les valeurs de l'axe y dans le premier graphique et un pour les valeurs de l'axe y dans le troisième graphique.

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```
