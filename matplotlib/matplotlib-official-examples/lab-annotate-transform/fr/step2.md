# Création de données

Ensuite, nous allons créer des données à tracer. Nous utiliserons la bibliothèque `numpy` pour créer une onde sinusoïdale.

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
