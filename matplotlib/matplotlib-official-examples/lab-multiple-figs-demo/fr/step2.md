# Création de données

Ensuite, nous devons créer des données à tracer. Nous allons créer deux ondes sinusoïdales que nous allons tracer dans des figures distinctes.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
```
