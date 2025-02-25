# Setzen des Zufallsziels und Generieren der Daten

In diesem Schritt setzen wir das Zufallsziel und generieren die Daten. Wir werden 100 Datenpunkte aus einer Normalverteilung mit einem Mittelwert von 200 und einer Standardabweichung von 25 generieren.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
