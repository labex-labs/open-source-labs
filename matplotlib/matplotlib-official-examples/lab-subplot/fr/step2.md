# Générer des données d'échantillonnage

Nous allons générer des données d'échantillonnage que nous utiliserons pour tracer nos graphiques.

```python
# Créez des données fictives.
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
x2 = np.linspace(0.0, 2.0)
y2 = np.cos(2 * np.pi * x2)
```
