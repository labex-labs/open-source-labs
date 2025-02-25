# Erstellen des Graphen

Jetzt können wir unseren Graphen erstellen. Wir werden einige Daten mit NumPy generieren und eine gedämpfte Exponentialabfallkurve darstellen.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
