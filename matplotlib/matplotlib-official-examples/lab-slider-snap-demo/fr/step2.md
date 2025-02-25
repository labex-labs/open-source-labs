# Générer des données

Dans cette étape, vous allez générer les données à tracer. Vous allez créer une onde sinusoïdale avec une fréquence de 3 Hz et une amplitude de 5.

```python
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)
```
