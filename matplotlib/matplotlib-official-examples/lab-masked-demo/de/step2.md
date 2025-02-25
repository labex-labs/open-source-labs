# Erstellen von Daten zum Plotten

Wir werden Daten zum Plotten mit NumPy erstellen. Wir werden 31 Datenpunkte zwischen -pi/2 und pi/2 generieren und den Kosinus dieser Werte hoch 3 berechnen.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```
