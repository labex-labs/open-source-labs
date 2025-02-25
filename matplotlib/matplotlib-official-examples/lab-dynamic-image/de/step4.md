# Generiere die Daten

Wir werden die `linspace`-Methode aus der Numpy-Bibliothek verwenden, um die Daten für die Animation zu generieren. Wir werden zwei Datensätze, `x` und `y`, generieren und dann die `y`-Daten umformen, um ein zweidimensionales Array zu erstellen.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
