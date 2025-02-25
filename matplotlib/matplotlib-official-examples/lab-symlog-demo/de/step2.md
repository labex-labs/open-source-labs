# Daten generieren

Als nächstes müssen wir einige Daten generieren, um sie zu plotten. In diesem Beispiel werden wir drei Arrays erstellen: eines für die x-Achsenwerte, eines für die y-Achsenwerte im ersten Plot und eines für die y-Achsenwerte im dritten Plot.

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```
