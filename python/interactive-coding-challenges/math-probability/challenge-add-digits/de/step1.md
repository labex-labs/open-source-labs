# Ziffern addieren

## Problem

Gegeben eine ganze Zahl müssen wir wiederholt ihre Ziffern addieren, bis das Ergebnis eine einzelne Ziffer ist. Beispielsweise, wenn uns die ganze Zahl 138 gegeben wird, addieren wir 1 + 3 + 8 = 12. Da 12 keine einzelne Ziffer ist, wiederholen wir den Vorgang und addieren 1 + 2 = 3. Daher ist das endgültige Ergebnis 3.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die eingegebene ganze Zahl ist nicht negativ.
- Die Eingaben sind nicht immer gültig, daher müssen wir alle auftretenden Fehler behandeln.
- Die Lösung sollte in den Arbeitsspeicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- Wenn wir None als Eingabe übergeben, sollte die Funktion einen TypeError auslösen.
- Wenn wir eine negative ganze Zahl als Eingabe übergeben, sollte die Funktion einen ValueError auslösen.
- Wenn wir 9 als Eingabe übergeben, sollte die Funktion 9 zurückgeben, da es bereits eine einzelne Ziffer ist.
- Wenn wir 138 als Eingabe übergeben, sollte die Funktion 3 zurückgeben.
- Wenn wir 65536 als Eingabe übergeben, sollte die Funktion 7 zurückgeben.
