# Création de données

Dans cette étape, nous allons créer des données à tracer. Nous utiliserons la fonction `squiggle_xy` pour générer des ondes sinusoïdales et cosinusoidales de fréquences différentes.

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
