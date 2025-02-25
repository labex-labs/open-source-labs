# Préparer les données

Nous allons générer deux ondes sinusoïdales avec des fréquences différentes à l'aide de NumPy.

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```
