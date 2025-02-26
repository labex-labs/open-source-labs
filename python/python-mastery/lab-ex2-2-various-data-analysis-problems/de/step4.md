# Data-Analyse-Aufgabe

Im letzten Lab haben Sie gerade Code geschrieben, um CSV-Daten im Zusammenhang mit der Chicago Transit Authority zu lesen. Beispielsweise können Sie die Daten als Dictionaries wie folgt abrufen:

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>>
```

Es wäre schade, all diese Arbeit zu verrichten und dann nichts mit den Daten zu tun.

In dieser Übung ist Ihre Aufgabe die folgende: Schreiben Sie ein Programm, um die folgenden vier Fragen zu beantworten:

1.  Wie viele Buslinien gibt es in Chicago?

2.  Wie viele Menschen haben am 2. Februar 2011 die Linie 22 genommen? Was ist mit einer beliebigen Linie zu einem beliebigen Datum Ihrer Wahl?

3.  Wie viele Fahrten wurden insgesamt auf jeder Buslinie genommen?

4.  Welche fünf Buslinien hatten den größten Anstieg in der Fahrgastzahl von 2001 bis 2011?

Sie können beliebige Techniken verwenden, um die obigen Fragen zu beantworten, solange es Teil der Python-Standardbibliothek ist (d.h. eingebauter Datentypen, Standardbibliotheksmodule usw.).
