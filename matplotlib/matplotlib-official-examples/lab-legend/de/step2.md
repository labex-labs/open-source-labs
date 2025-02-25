# Generieren der Daten

Als nächstes werden wir einige simulierte Daten generieren, die wir in unserem Diagramm verwenden. Wir werden zwei Arrays, `a` und `b`, mit der NumPy-Funktion `arange` erstellen. Anschließend berechnen wir zwei weitere Arrays, `c` und `d`, wobei wir die `exp`-Funktion verwenden, um die Exponentialwerte von `a` zu berechnen und `d` als das Umgekehrte von `c` zu berechnen.

```python
# Make some fake data.
a = b = np.arange(0, 3,.02)
c = np.exp(a)
d = c[::-1]
```
