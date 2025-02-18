# Erstellen der Daten

Wir werden nun einige Zufallsdaten erstellen, die Ausreißer enthalten. Wir verwenden `numpy.random.rand`, um 30 Zufallszahlen zu generieren und fügen dann zwei Ausreißer zu den Daten hinzu.

```python
np.random.seed(19680801)

pts = np.random.rand(30)*.2
# Jetzt erstellen wir zwei Ausreißerpunkte, die weit von allen anderen entfernt sind.
pts[[3, 14]] +=.8
```
