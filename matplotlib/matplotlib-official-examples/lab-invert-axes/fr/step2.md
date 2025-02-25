# Création de données

Ensuite, nous devons créer des données à tracer. Dans cet exemple, nous allons créer un tableau de valeurs pour le temps (`t`) et un tableau de valeurs pour la tension (`s`).

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```
