# Überprüfen, ob ein Datum ein Werktag ist

## Problem

Schreibe eine Python-Funktion namens `is_weekday()`, die ein Datum als Eingabe erhält und `True` zurückgibt, wenn es ein Werktag ist, und `False`, wenn es ein Wochenende ist. Wenn kein Datum angegeben wird, soll die Funktion das aktuelle Datum verwenden.

Um dieses Problem zu lösen, kannst du die folgenden Schritte ausführen:

1. Importiere das Modul `datetime`.
2. Definiere eine Funktion namens `is_weekday()`, die ein Datum als Eingabe erhält. Wenn kein Datum angegeben wird, verwende das aktuelle Datum.
3. Verwende die Methode `weekday()` des Moduls `datetime`, um den Wochentag als Ganzzahl zu erhalten. Die Methode `weekday()` gibt eine Ganzzahl zwischen 0 (Montag) und 6 (Sonntag) zurück.
4. Überprüfe, ob der Wochentag kleiner oder gleich 4 ist. Wenn ja, gib `True` zurück, andernfalls gib `False` zurück.

## Beispiel

Hier sind einige Beispiele dafür, wie deine Funktion verhalten sollte:

```python
from datetime import date

assert is_weekday(date(2022, 11, 11)) == False
assert is_weekday(date(2022, 11, 14)) == True
assert is_weekday(date(2022, 11, 12)) == False
assert is_weekday(date(2022, 11, 13)) == False
```
