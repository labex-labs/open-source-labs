# Übung 9.2: Erstellen eines Anwendungsverzeichnisses

Das Einbringen Ihres gesamten Codes in ein "Paket" reicht für eine Anwendung oft nicht aus. Manchmal gibt es unterstützende Dateien, Dokumentation, Skripte und andere Dinge. Diese Dateien müssen außerhalb des oben erstellten `porty/`-Verzeichnisses existieren.

Erstellen Sie ein neues Verzeichnis namens `porty-app`. Verschieben Sie das in Übung 9.1 erstellte `porty`-Verzeichnis in dieses Verzeichnis. Kopieren Sie die Testdateien `portfolio.csv` und `prices.csv` in dieses Verzeichnis. Erstellen Sie zusätzlich eine `README.txt`-Datei mit Informationen über sich selbst. Ihr Code sollte jetzt wie folgt organisiert sein:

    porty-app/
        portfolio.csv
        prices.csv
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py

Um Ihren Code auszuführen, müssen Sie sicherstellen, dass Sie im obersten Level-Verzeichnis `porty-app/` arbeiten. Beispielsweise von der Kommandozeile:

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

Versuchen Sie, einige Ihrer vorherigen Skripte als Hauptprogramm auszuführen:

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

$
```
