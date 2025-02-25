# Rauschen zu den Daten hinzufügen

In diesem Schritt werden wir unserem Datensatz etwas Rauschen hinzufügen, um es realistischer zu gestalten. Wir werden die `normal`-Funktion von NumPy verwenden, um Zufallszahlen mit einem Mittelwert von 0,0 und einer Standardabweichung von 0,3 zu generieren.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
