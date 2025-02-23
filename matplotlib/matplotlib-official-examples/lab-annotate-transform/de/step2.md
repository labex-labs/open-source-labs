# Daten erstellen

Als nächstes werden wir einige Daten erstellen, um ein Diagramm zu plotten. Wir werden die Bibliothek `numpy` verwenden, um eine Sinuswelle zu erstellen.

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
