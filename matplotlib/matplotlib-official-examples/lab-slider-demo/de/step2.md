# Die Sinuswellenfunktion definieren

Als nächstes definieren wir die Funktion, die unsere Sinuswelle erzeugen wird. Die Funktion nimmt zwei Parameter entgegen, Amplitude und Frequenz, und gibt die Sinuswelle zu einem bestimmten Zeitpunkt zurück.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
