# Stapel Min

## Problem

Das Problem besteht darin, einen Stapel mit push-, pop- und min-Methoden zu implementieren, die in O(1)-Zeit laufen. Die push-Methode fügt ein Element zur Sammlung hinzu, die pop-Methode entfernt das zuletzt hinzugefügte Element, das noch nicht entfernt wurde, und die min-Methode gibt das kleinste Element im Stapel zurück. Alle drei Methoden sollten in konstanter Zeit, O(1), laufen.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Der Stapel enthält nur Ganzzahlen.
- Die Eingabewerte für push sind gültig.
- Wenn wir die min-Methode auf einem leeren Stapel aufrufen, sollten wir sys.maxsize zurückgeben.
- Wir können davon ausgehen, dass wir bereits eine Stapelklasse haben, die für dieses Problem verwendet werden kann.
- Wir können davon ausgehen, dass der Stapel in den Arbeitsspeicher passt.

## Beispielverwendung

Wir können unsere Implementierung mit den folgenden Szenarien testen:

- Push/Pop auf einem leeren Stapel.
- Push/Pop auf einem nicht-leeren Stapel.
- Min auf einem leeren Stapel.
- Min auf einem nicht-leeren Stapel.
