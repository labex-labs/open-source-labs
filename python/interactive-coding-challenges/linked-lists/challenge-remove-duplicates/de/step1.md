# Duplikate entfernen

## Problem

Gegeben eine nicht-zirkuläre, singulär verkettete Liste, entferne die Duplikate daraus. Ziel ist es, die ursprüngliche Liste in-place zu modifizieren und den Kopf der modifizierten Liste zurückzugeben.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die verkettete Liste ist nicht-zirkulär und singulär verkettet.
- Es dürfen keine `None`-Werte in die Liste eingefügt werden.
- Wir haben bereits eine Klasse für verkettete Listen, die für dieses Problem verwendet werden kann.
- Es müssen zwei Lösungen implementiert werden: eine mit zusätzlichen Datenstrukturen und eine ohne.
- Das Problem passt in den Speicher.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verhalten sollte:

- Leere verkettete Liste -> []
- Verkettete Liste mit einem Element -> [Element]
- Allgemeiner Fall ohne Duplikate -> [1, 2, 3, 4]
- Allgemeiner Fall mit Duplikaten -> [1, 2, 3]
