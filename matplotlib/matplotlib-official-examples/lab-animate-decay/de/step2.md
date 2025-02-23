# Die Datengenerierungsfunktion erstellen

Als nächstes müssen wir eine Funktion erstellen, die die Daten für die Animation generiert. Die Funktion wird eine Sinuswelle erzeugen, die im Laufe der Zeit abnimmt. Wir werden die `itertools.count()`-Funktion verwenden, um eine unendliche Zahlenfolge zu generieren. Wir werden diese Zahlen verwenden, um die Werte der Sinuswelle zu berechnen.

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
