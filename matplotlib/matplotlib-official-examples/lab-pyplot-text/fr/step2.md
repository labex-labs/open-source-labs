# Création de données

Ensuite, nous allons créer des données pour le tracé. Nous allons créer une onde sinusoïdale à l'aide de la bibliothèque `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
```
