# Générer des données

Nous générons quelques données d'échantillonnage à tracer. Ici, nous utilisons la bibliothèque `numpy` pour générer trois tableaux de données.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
