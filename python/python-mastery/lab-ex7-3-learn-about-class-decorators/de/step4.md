# Hinzufügen von Funktionalität zur Zeilenkonvertierung

In der Programmierung ist es oft nützlich, Instanzen einer Klasse aus Datenzeilen zu erstellen, insbesondere wenn man mit Daten aus Quellen wie CSV-Dateien arbeitet. In diesem Abschnitt fügen wir die Möglichkeit hinzu, Instanzen der `Structure`-Klasse aus Datenzeilen zu erstellen. Wir werden dies tun, indem wir eine Klassenmethode `from_row` in der `Structure`-Klasse implementieren.

1. Zunächst müssen Sie die Datei `structure.py` öffnen. Hier werden wir unsere Codeänderungen vornehmen. Verwenden Sie den folgenden Befehl in Ihrem Terminal:

```bash
code ~/project/structure.py
```

2. Als Nächstes werden wir die Funktion `validate_attributes` ändern. Diese Funktion ist ein Klassen-Dekorator (class decorator), der `Validator`-Instanzen extrahiert und die Listen `_fields` und `_types` automatisch erstellt. Wir werden sie aktualisieren, um auch Typinformationen zu sammeln.

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

In dieser aktualisierten Funktion sammeln wir das `expected_type`-Attribut von jedem Validator und speichern es in der Klassenvariablen `_types`. Dies wird später nützlich sein, wenn wir Daten aus Zeilen in die richtigen Typen umwandeln.

3. Jetzt fügen wir die Klassenmethode `from_row` zur `Structure`-Klasse hinzu. Diese Methode ermöglicht es uns, eine Instanz der Klasse aus einer Datenzeile zu erstellen, die eine Liste oder ein Tupel sein kann.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

So funktioniert diese Methode:

- Sie nimmt eine Datenzeile entgegen, die in Form einer Liste oder eines Tupels vorliegen kann.
- Sie wandelt jeden Wert in der Zeile in den erwarteten Typ um, indem sie die entsprechende Funktion aus der `_types`-Liste verwendet.
- Sie erstellt dann eine neue Instanz der Klasse mit den umgewandelten Werten und gibt sie zurück.

4. Nach diesen Änderungen speichern Sie die Datei `structure.py`. Dadurch werden Ihre Codeänderungen beibehalten.

5. Lassen Sie uns unsere `from_row`-Methode testen, um sicherzustellen, dass sie wie erwartet funktioniert. Wir werden einen einfachen Test mit der `Stock`-Klasse durchführen. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Beachten Sie, dass die Zeichenkettenwerte '100' und '490.1' automatisch in die richtigen Typen (Integer und Float) umgewandelt wurden. Dies zeigt, dass unsere `from_row`-Methode korrekt funktioniert.

6. Schließlich versuchen wir, Daten aus einer CSV-Datei mit unserem `reader.py`-Modul zu lesen. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

Sie sollten eine Ausgabe sehen, die die Aktien aus der CSV-Datei anzeigt:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

Die `from_row`-Methode ermöglicht es uns, CSV-Daten einfach in Instanzen der `Stock`-Klasse umzuwandeln. In Kombination mit der Funktion `read_csv_as_instances` haben wir eine leistungsstarke Möglichkeit, strukturierte Daten zu laden und zu verarbeiten.
