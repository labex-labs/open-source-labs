# Neuzuweisung vs Änderung

Stellen Sie sicher, dass Sie den subtilen Unterschied zwischen der Änderung eines Werts und der Neuzuweisung eines Variablennamens verstehen.

```python
def foo(items):
    items.append(42)    # Ändert das Eingabeelement

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Ändert die lokale Variable `items`, sodass sie auf ein anderes Objekt zeigt

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

_Hinweis: Die Variablennzuweisung überschreibt niemals das Speicher. Der Name wird lediglich an einen neuen Wert gebunden._

In dieser Reihe von Übungen implementieren Sie möglicherweise den mächtigsten und schwierigsten Teil des Kurses. Es gibt viele Schritte und viele Konzepte aus früheren Übungen werden auf einmal zusammengeführt. Die endgültige Lösung umfasst nur etwa 25 Zeilen Code, aber nehmen Sie sich Ihren Zeit und stellen Sie sicher, dass Sie jeden Teil verstehen.

Ein zentraler Teil Ihres `report.py`-Programms konzentriert sich auf das Lesen von CSV-Dateien. Beispielsweise liest die Funktion `read_portfolio()` eine Datei, die Zeilen mit Portfolio-Daten enthält, und die Funktion `read_prices()` liest eine Datei, die Zeilen mit Preisdaten enthält. In beiden Funktionen gibt es viele niedrigere "umständliche" Teile und ähnliche Merkmale. Beispielsweise öffnen sie beide eine Datei und umschließen sie mit dem `csv`-Modul und sie konvertieren verschiedene Felder in neue Typen.

Wenn Sie viel Datei-Parsing im echten Leben machen würden, würden Sie wahrscheinlich einige dieser Dinge aufräumen und es allgemeiner einsetzbar machen wollen. Das ist unser Ziel.

Beginnen Sie diese Übung, indem Sie die Datei `fileparse.py` öffnen. Hier werden wir unsere Arbeit verrichten.
