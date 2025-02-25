# Créer des données

Dans cette étape, nous allons créer un dictionnaire `data` contenant des valeurs pour les variables `a`, `b`, `c` et `d`.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
