# Créez le tracé

Maintenant, nous pouvons créer notre tracé. Nous allons générer des données à l'aide de NumPy et tracer une courbe d'amortissement d'exponentielle décroissante.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
