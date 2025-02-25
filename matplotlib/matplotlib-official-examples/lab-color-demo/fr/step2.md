# Définir les données

Ensuite, nous devons définir les données que nous utiliserons pour notre graphique. Nous allons créer une onde sinusoïdale avec 201 points de données :

```python
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
```
