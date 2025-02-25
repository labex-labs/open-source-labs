# Création de tableaux linéaires et non linéaires

Nous devons créer deux tableaux, l'un avec des valeurs linéaires et l'autre avec des valeurs non linéaires. Ces tableaux seront utilisés pour créer notre NonUniformImage.

```python
# Tableau linéaire x pour les centres des cellules :
x = np.linspace(-4, 4, 9)

# Tableau x hautement non linéaire :
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
