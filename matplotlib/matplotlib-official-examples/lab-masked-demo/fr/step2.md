# Créez des données pour le tracé

Nous allons créer des données pour le tracé à l'aide de NumPy. Nous allons générer 31 points de données entre -pi/2 et pi/2 et calculer le cosinus de ces valeurs élevées à la puissance 3.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```
