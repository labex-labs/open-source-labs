# Création de tableaux masqués

Dans cette étape, nous allons créer trois tableaux masqués : l'un pour les valeurs supérieures à un certain seuil, l'un pour les valeurs inférieures à un certain seuil et l'un pour les valeurs comprises entre deux seuils.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
