# Daten erstellen

Als nächstes werden wir einige Daten erstellen, um sie zu plotten. In diesem Beispiel werden wir die Sinusfunktion verwenden, um eine Welle zu generieren.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
```
