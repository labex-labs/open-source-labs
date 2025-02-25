# Gib Binärdarstellung aus

## Problemstellung

Schreibe eine Python-Funktion, die eine reelle Zahl zwischen 0 und 1 als Eingabe erhält und ihre binäre Darstellung als Zeichenfolge zurückgibt. Wenn die Länge der Darstellung größer als 32 ist, gebe 'FEHLER' zurück.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen gewährleisten:

- Die Eingabe muss ein Float sein.
- Die Ausgabe muss eine Zeichenfolge sein.
- Der Bereich der Eingabe liegt zwischen 0 und 1, wobei die Werte 0 und 1 nicht eingeschlossen sind.
- Das Ergebnis muss ein Nachkommastelle und ein Nachkommastandard enthalten.
- Die führende Null und die Dezimalpunktzahl werden bei der 32-Zeichen-Grenze berücksichtigt.
- Wir können nicht davon ausgehen, dass die Eingaben gültig sind.
- Wir können davon ausgehen, dass das Programm im Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie die Funktion verhalten sollte:

- Keine Eingabe -> 'FEHLER'
- Außerhalb der Grenzen (0, 1) -> 'FEHLER'
- 0.625 -> 0.101
- 0.987654321 -> 'FEHLER'
