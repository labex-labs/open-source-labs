# Übung 1.28: Andere Arten von "Dateien"

Was passiert, wenn Sie eine nicht-textuelle Datei wie eine gzip-komprimierte Daten-Datei lesen möchten? Die eingebaut-funktion `open()` hilft Ihnen hier nicht weiter, aber Python hat ein Bibliotheksmodul `gzip`, das gzip-komprimierte Dateien lesen kann.

Versuchen Sie es:

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... schauen Sie sich die Ausgabe an...
>>>
```

Hinweis: Das Einbeziehen des Dateimodus `'rt'` ist hier von entscheidender Bedeutung. Wenn Sie das vergessen, erhalten Sie Bytezeichenketten anstelle von normalen Textzeichenketten.
