# Die Emitter-Funktion erstellen

Die `emitter`-Funktion generiert die Daten, die an die `update`-Methode übergeben werden. In diesem Fall generieren wir Zufallsdaten mit einer Wahrscheinlichkeit von 0,1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
