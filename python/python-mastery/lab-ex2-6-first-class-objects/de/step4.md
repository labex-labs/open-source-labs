# Sonderaufgabe Projekt

In Übung 2.5 haben wir eine Klasse `RideData` erstellt, die alle Busdaten in Spalten gespeichert hat, aber die Daten tatsächlich als eine Sequenz von Dictionaries an einen Benutzer präsentiert hat. Dadurch wurde durch verschiedene Formen von Magie viel Speicher eingespart.

Können Sie diese Idee verallgemeinern? Insbesondere, können Sie eine allgemeine Funktion `read_csv_as_columns()` erstellen, die so funktioniert:

```python
>>> data = read_csv_as_columns('ctabus.csv', types=[str, str, str, int])
>>> data
<__main__.DataCollection Objekt am 0x102b45048>
>>> len(data)
577563
>>> data[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> data[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Diese Funktion soll allgemein einsetzbar sein - Sie können ihr jede Datei und eine Liste der Spaltentypen geben, und sie wird die Daten lesen. Die Daten werden in eine Klasse `DataCollection` gelesen, die die Daten intern als Spalten speichert. Die Daten präsentieren sich jedoch als eine Sequenz von Dictionaries, wenn sie abgerufen werden.

Versuchen Sie, diese Funktion mit dem Trick der Zeichenketteninternierung im letzten Teil zu verwenden. Wie viel Speicher benötigt es jetzt, um alle Fahrdaten zu speichern? Können Sie diese Funktion weiterhin mit Ihrem früheren CTA-Analysecode verwenden?

## Hinweis:

Vervollständigen Sie die Funktion `read_csv_as_columns()` in der Datei `colreader.py`.
