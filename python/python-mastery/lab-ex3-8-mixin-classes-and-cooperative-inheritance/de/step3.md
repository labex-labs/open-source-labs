# Erstellung einer benutzerfreundlichen API für Mixins

Mixins sind leistungsstark, aber die direkte Verwendung von Mehrfachvererbung (multiple inheritance) kann sich komplex anfühlen. In diesem Schritt werden wir die Funktion `create_formatter()` verbessern, um diese Komplexität zu verbergen und eine einfachere API für Benutzer bereitzustellen.

Stellen Sie zunächst sicher, dass `tableformat.py` in Ihrem Editor geöffnet ist:

```bash
cd ~/project
touch tableformat.py
```

Suchen Sie die vorhandene Funktion `create_formatter()`:

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Ersetzen Sie die _gesamte vorhandene_ Funktionsdefinition `create_formatter()` durch die unten stehende erweiterte Version. Diese neue Version akzeptiert optionale Argumente für Spaltenformate und die Umwandlung von Headern in Großbuchstaben.

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_Selbstkorrektur: Erstellen Sie das Klassentupel für die Vererbung dynamisch anstelle von mehreren if/elif-Zweigen._

Diese erweiterte Funktion bestimmt zunächst die Basisformatiererklasse (`TextTableFormatter`, `CSVTableFormatter` usw.). Dann konstruiert sie basierend auf den optionalen Argumenten `column_formats` und `upper_headers` dynamisch eine neue Klasse (`CustomFormatter`), die von den erforderlichen Mixins und der Basisformatiererklasse erbt. Schließlich gibt sie eine Instanz dieses benutzerdefinierten Formatierers zurück.

**Denken Sie daran, die Änderungen an `tableformat.py` zu speichern.**

Lassen Sie uns nun unsere erweiterte Funktion testen. **Stellen Sie sicher, dass Sie die aktualisierte Funktion `create_formatter` in `tableformat.py` gespeichert haben.**

Testen Sie zunächst die Spaltenformatierung. Erstellen Sie `step3_test1.py`:

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

Führen Sie das Skript aus:

```bash
python3 step3_test1.py
```

Sie sollten die Tabelle mit formatierten Spalten sehen (wiederum vorbehaltlich der Typbehandlung des Preisformats):

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

Testen Sie als Nächstes die Großbuchstaben-Header. Erstellen Sie `step3_test2.py`:

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

Führen Sie das Skript aus:

```bash
python3 step3_test2.py
```

Sie sollten die Tabelle mit Großbuchstaben-Headern sehen:

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

Kombinieren Sie schließlich beide Optionen. Erstellen Sie `step3_test3.py`:

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

Führen Sie das Skript aus:

```bash
python3 step3_test3.py
```

Dies sollte eine Tabelle mit sowohl formatierten Spalten als auch Großbuchstaben-Headern anzeigen:

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
------------------------------------------------------------------
```

Die erweiterte Funktion funktioniert auch mit anderen Formatierertypen. Probieren Sie sie beispielsweise mit dem CSV-Formatierer aus. Erstellen Sie `step3_test4.py`:

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

Führen Sie das Skript aus:

```bash
python3 step3_test4.py
```

Dies sollte Großbuchstaben-Header und formatierte Spalten im CSV-Format erzeugen (wiederum potenzielles Typproblem für die `%d`/`%.2f`-Formatierung von Strings, die von `print_table` übergeben werden):

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

Durch die Erweiterung der Funktion `create_formatter()` haben wir eine benutzerfreundliche API erstellt. Benutzer können nun auf einfache Weise Mixin-Funktionen anwenden, ohne die Mehrfachvererbungsstruktur selbst verwalten zu müssen.
