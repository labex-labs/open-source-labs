# Tiefe Überlegung

In dieser Übung haben Sie zwei Funktionen geschrieben, `read_csv_as_dicts()` und `read_csv_as_columns()`. Diese Funktionen präsentieren die Daten auf die gleiche Weise an den Benutzer. Beispielsweise:

```python
>>> data1 = read_csv_as_dicts('ctabus.csv', [str, str, str, int])
>>> len(data1)
577563
>>> data1[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data1[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>

>>> data2 = read_csv_as_columns('ctabus.csv', [str, str, str, int])
>>> len(data2)
577563
>>> data2[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data2[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```

Tatsächlich können Sie jede dieser Funktionen im CTA-Analysecode verwenden, den Sie geschrieben haben. Dennoch passieren unter der Haube völlig verschiedene Dinge. Die Funktion `read_csv_as_columns()` speichert die Daten in einer anderen Darstellung. Sie stützt sich auf die Python-Sequenzprotokolle (Magie-Methoden), um Ihnen die Informationen auf eine nützlichere Weise zu präsentieren.

Dies ist tatsächlich Teil eines viel größeren Programmierkonzepts der "Datenabstraktion". Wenn Sie Programme schreiben, ist die Art, wie die Daten präsentiert werden, oft wichtiger als, wie die Daten tatsächlich zusammengebaut werden. Obwohl wir die Daten als eine Sequenz von Dictionaries präsentieren, gibt es eine große Flexibilität darin, wie das tatsächlich im Hintergrund passiert. Das ist eine mächtige Idee und etwas, über das Sie nachdenken sollten, wenn Sie Ihre eigenen Programme schreiben.
