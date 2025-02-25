# Générer des données

Ensuite, vous allez générer quelques données d'échantillonnage. Dans ce laboratoire, nous allons générer une onde sinusoïdale bidimensionnelle.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
