# Fehlende Ganzzahl finden

## Problem

Gegeben ein Array von 32 nicht-negativen ganzen Zahlen, finde eine Ganzzahl, die nicht im Eingabearray enthalten ist. Die Lösung sollte minimalen Speicher verwenden.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Das Eingabearray enthält nicht-negativen ganze Zahlen.
- Der Bereich der ganzen Zahlen ist nicht angegeben, aber wir müssen den Ansatz für 4 Milliarden ganze Zahlen diskutieren.
- Wir müssen die Lösung für ein Array von 32 ganzen Zahlen implementieren.
- Wir dürfen nicht annehmen, dass das Eingabearray gültig ist.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verhalten sollte:

- Wenn die Eingabe None oder ein leeres Array ist, sollte die Funktion eine Ausnahme auslösen.
- Wenn es eine Ganzzahl gibt, die aus dem Eingabearray ausgeschlossen ist, sollte die Funktion diese Ganzzahl zurückgeben.
- Wenn es keine Ganzzahl gibt, die aus dem Eingabearray ausgeschlossen ist, sollte die Funktion None zurückgeben.
