# Zwei subtrahieren

## Problem

Schreiben Sie eine Python-Funktion, die zwei ganze Zahlen als Eingabe annimmt und deren Differenz ohne das '+' - oder '-' -Zeichen zurückgibt. Die Funktion sollte die folgenden Fälle behandeln:

- Wenn eine der Eingaben None ist, sollte die Funktion einen TypeError auslösen.
- Die Funktion sollte sowohl für positive als auch negative ganze Zahlen funktionieren.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen beachten:

- Überprüfen Sie auf None-Eingaben und werfen Sie gegebenenfalls einen TypeError.
- Wir können davon ausgehen, dass die Eingaben in den Speicher passen.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie die Funktion verhalten sollte:

```
sub_two(None, 5) -> TypeError
sub_two(7, 5) -> 2
sub_two(-5, -7) -> 2
sub_two(-5, 7) -> -12
sub_two(5, -7) -> 12
```
