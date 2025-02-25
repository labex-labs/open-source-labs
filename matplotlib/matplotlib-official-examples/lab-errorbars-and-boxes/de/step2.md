# Daten vorbereiten

Anschließend werden wir die Daten für unseren Boxplot vorbereiten. Wir werden einige Platzhalterdaten für die x- und y-Werte sowie die Fehlerwerte erstellen.

```python
# Anzahl der Datenpunkte
n = 5

# Platzhalterdaten
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# Dummy-Fehler (oben und unten)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
