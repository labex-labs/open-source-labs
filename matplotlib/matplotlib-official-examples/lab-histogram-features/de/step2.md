# Generieren von Beispiel-Daten

In diesem Schritt werden wir Beispiel-Daten mit numpy generieren. Wir werden zufällige Daten aus einer Normalverteilung mit einem Mittelwert von 100 und einer Standardabweichung von 15 generieren.

```python
np.random.seed(19680801)
mu = 100  # Mittelwert der Verteilung
sigma = 15  # Standardabweichung der Verteilung
x = mu + sigma * np.random.randn(437)
```
