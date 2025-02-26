# Übung 9.1: Erstellen eines einfachen Pakets

Erstellen Sie ein Verzeichnis namens `porty/` und legen Sie alle obigen Python-Dateien darin ab. Erstellen Sie zusätzlich eine leere `__init__.py`-Datei und legen Sie sie im Verzeichnis ab. Sie sollten ein Verzeichnis mit Dateien wie dieses haben:

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

Löschen Sie die Datei `__pycache__`, die sich in Ihrem Verzeichnis befindet. Dies enthält zuvor kompilierte Python-Module. Wir möchten von vorne beginnen.

Versuchen Sie, einige der Paketmodule zu importieren:

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

Wenn diese Imports fehlschlagen, gehen Sie in die entsprechende Datei und ändern Sie die Modulimporte, um einen paketrelativen Import zu verwenden. Beispielsweise könnte ein Statement wie `import fileparse` wie folgt geändert werden:

    # report.py
    from. import fileparse

...

Wenn Sie ein Statement wie `from fileparse import parse_csv` haben, ändern Sie den Code wie folgt:

    # report.py
    from.fileparse import parse_csv

...
