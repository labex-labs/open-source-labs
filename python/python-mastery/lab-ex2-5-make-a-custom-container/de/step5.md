# Herausforderung

Was passiert, wenn Sie einen Ausschnitt aus den Fahrtdaten nehmen?

```python
>>> r = rows[0:10]
>>> r
... schauen Sie sich das Ergebnis an...
>>>
```

Es wird wahrscheinlich ein bisschen verrückt aussehen. Können Sie die `RideData`-Klasse so modifizieren, dass sie einen korrekten Ausschnitt produziert, der wie eine Liste von Wörterbüchern aussieht? Beispielsweise wie folgt:

```python
>>> rows = readrides.read_rides_as_columns('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> r = rows[0:10]
>>> r
<readrides.RideData object at 0x10f5068c8>
>>> len(r)
10
>>> r[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> r[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```
