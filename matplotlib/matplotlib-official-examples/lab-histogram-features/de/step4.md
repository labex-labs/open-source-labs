# Fügen Sie eine Linie mit der besten Anpassung hinzu

In diesem Schritt werden wir einer Linie mit der besten Anpassung zum Histogramm hinzufügen. Wir werden die y-Werte für die Linie berechnen und sie über dem Histogramm plotten.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
