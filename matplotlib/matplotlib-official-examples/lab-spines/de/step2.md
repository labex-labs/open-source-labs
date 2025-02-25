# Beispielsdaten erstellen

Als nächstes werden wir mit NumPy Beispielsdaten für unseren Graphen erstellen. Wir werden 100 Datenpunkte zwischen 0 und 2π generieren und deren zugehörige Sinuswerte berechnen.

```python
x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)
```
