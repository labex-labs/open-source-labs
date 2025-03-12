# Hinzufügen von Typ-Hinweisen

In Python 3.5 und späteren Versionen werden Typ-Hinweise (type hints) unterstützt. Typ-Hinweise sind eine Möglichkeit, die erwarteten Datentypen von Variablen, Funktionsparametern und Rückgabewerten in Ihrem Code anzugeben. Sie ändern nicht, wie der Code ausgeführt wird, sondern machen den Code lesbarer und können helfen, bestimmte Arten von Fehlern zu erkennen, bevor der Code tatsächlich ausgeführt wird. Jetzt fügen wir Typ-Hinweise zu unseren CSV-Reader-Funktionen hinzu.

1. Öffnen Sie die `reader.py`-Datei und aktualisieren Sie sie, um Typ-Hinweise einzubeziehen:

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

Lassen Sie uns die wichtigsten Änderungen verstehen, die wir im Code vorgenommen haben:

1. Wir haben Typen aus dem `typing`-Modul importiert. Dieses Modul bietet eine Reihe von Typen, die wir verwenden können, um Typ-Hinweise zu definieren. Beispielsweise sind `List`, `Dict` und `Optional` Typen aus diesem Modul.
2. Wir haben eine generische Typvariable `T` hinzugefügt, um den Klassentyp darzustellen. Eine generische Typvariable ermöglicht es uns, Funktionen zu schreiben, die auf sichere Weise mit verschiedenen Typen arbeiten können.
3. Wir haben Typ-Hinweise zu allen Funktionsparametern und Rückgabewerten hinzugefügt. Dies macht klar, welche Typen von Argumenten eine Funktion erwartet und welchen Typ von Wert sie zurückgibt.
4. Wir haben geeignete Containertypen wie `List`, `Dict` und `Optional` verwendet. `List` repräsentiert eine Liste, `Dict` ein Wörterbuch und `Optional` gibt an, dass ein Parameter entweder einen bestimmten Typ haben oder `None` sein kann.
5. Wir haben `Callable` für die Typkonvertierungsfunktionen verwendet. `Callable` wird verwendet, um anzugeben, dass ein Parameter eine aufrufbare Funktion ist.
6. Wir haben das generische `T` verwendet, um auszudrücken, dass `csv_as_instances` eine Liste von Instanzen der übergebenen Klasse zurückgibt. Dies hilft der IDE und anderen Tools, den Typ der zurückgegebenen Objekte zu verstehen.

7. Jetzt erstellen wir eine einfache Testdatei, um sicherzustellen, dass alles weiterhin richtig funktioniert:

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. Führen Sie das Testskript aus dem Terminal aus:

```bash
python test_types.py
```

Die Ausgabe sollte in etwa so aussehen:

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

Typ-Hinweise ändern nicht, wie der Code ausgeführt wird, sondern bieten mehrere Vorteile:

1. Sie bieten eine bessere IDE-Unterstützung mit Code-Vervollständigung. Wenn Sie eine IDE wie PyCharm oder VS Code verwenden, kann diese die Typ-Hinweise nutzen, um die richtigen Methoden und Attribute für Ihre Variablen vorzuschlagen.
2. Sie liefern klarere Dokumentation über die erwarteten Parameter- und Rückgabetypen. Nur durch Betrachten der Funktionsdefinition können Sie feststellen, welche Typen von Argumenten sie erwartet und welchen Typ von Wert sie zurückgibt.
3. Sie ermöglichen es Ihnen, statische Typ-Checker wie mypy zu verwenden, um Fehler frühzeitig zu erkennen. Statische Typ-Checker analysieren Ihren Code, ohne ihn auszuführen, und können typbezogene Fehler finden, bevor Sie den Code ausführen.
4. Sie verbessern die Lesbarkeit und Wartbarkeit des Codes. Wenn Sie oder andere Entwickler später wieder zum Code zurückkehren, ist es einfacher zu verstehen, was der Code tut.

In einer großen Codebasis können diese Vorteile die Anzahl von Fehlern erheblich reduzieren und den Code leichter verständlich und wartbar machen.

**Hinweis:** Typ-Hinweise sind in Python optional, werden aber zunehmend in professionellem Code verwendet. Bibliotheken wie die im Python-Standardbibliothek und viele beliebte Drittanbieter-Pakete enthalten jetzt umfangreiche Typ-Hinweise.
