# Zweierpotenz

## Problem

Schreiben Sie eine Python-Funktion namens `is_power_of_two`, die einen Integer als Parameter annimmt und `True` zurückgibt, wenn die Eingabe eine Zweierpotenz ist, und `False` sonst. Eine Zweierpotenz ist jede Zahl, die als 2^n dargestellt werden kann, wobei n ein Integer ist. Beispielsweise sind 2, 4, 8 und 16 alle Zweierpotenzen.

## Anforderungen

Die `is_power_of_two`-Funktion muss die folgenden Anforderungen erfüllen:

- Die Eingabzahl muss ein Integer sein.
- Die Funktion muss ungültige Eingaben优雅地 (gracefully) behandeln.
- Die Ausgabe muss ein Boolean sein.
- Die Funktion muss innerhalb der Speicherbeschränkungen passen.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie die `is_power_of_two`-Funktion verhalten sollte:

- `is_power_of_two(None)` sollte einen `TypeError` auslösen.
- `is_power_of_two(0)` sollte `False` zurückgeben.
- `is_power_of_two(1)` sollte `True` zurückgeben.
- `is_power_of_two(2)` sollte `True` zurückgeben.
- `is_power_of_two(15)` sollte `False` zurückgeben.
- `is_power_of_two(16)` sollte `True` zurückgeben.
