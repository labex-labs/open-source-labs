# Ein Kontext-Manager

In Übung 3.5 haben Sie es Benutzern ermöglicht, schön formattierte Tabellen zu erstellen. Beispielsweise:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Ein Problem mit dem Code ist, dass alle Tabellen auf die Standardausgabe (`sys.stdout`) gedruckt werden. Nehmen Sie an, Sie möchten die Ausgabe an eine Datei oder an einen anderen Ort umleiten. Im Großen und Ganzen könnten Sie den gesamten Tabellenformatierungs-Code ändern, um eine andere Ausgabedatei zuzulassen. Im Notfall könnten Sie dies jedoch auch mit einem Kontext-Manager lösen.

Definieren Sie folgenden Kontext-Manager:

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

Dieser Kontext-Manager funktioniert, indem er einen temporären Patch auf `sys.stdout` anwendet, um alle Ausgabe an eine andere Datei umzuleiten. Beim Verlassen des Kontexts wird der Patch rückgängig gemacht. Testen Sie es:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # Überprüfen Sie die Datei
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
