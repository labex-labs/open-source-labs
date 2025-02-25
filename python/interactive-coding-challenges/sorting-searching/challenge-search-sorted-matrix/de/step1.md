# Sortierte Matrix durchsuchen

## Problem

Gegeben eine sortierte Matrix müssen wir darin ein bestimmtes Element suchen. Die Matrix ist so sortiert, dass die Elemente in jeder Zeile und Spalte in aufsteigender Reihenfolge sortiert sind. Die Matrix muss nicht notwendigerweise eine quadratische Matrix sein. Wir müssen die Position des Elements in der Matrix als Tupel (Zeile, Spalte) zurückgeben, wenn es gefunden wird, andernfalls müssen wir None zurückgeben.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Annahmen machen:

- Die Elemente in jeder Zeile der Matrix sind in aufsteigender Reihenfolge sortiert.
- Die Elemente in jeder Spalte der Matrix sind in aufsteigender Reihenfolge sortiert.
- Die Matrix ist nicht zerrig, d.h. es handelt sich um ein Rechteck.
- Die Sortierreihenfolge ist aufsteigend.
- Die Matrix muss nicht notwendigerweise eine quadratische Matrix sein.
- Die Ausgabe ist ein Tupel (Zeile, Spalte).
- Das Element, das wir suchen, kann in der Matrix vorhanden sein oder nicht.
- Die Eingaben können gültig oder ungültig sein.
- Die Lösung sollte in den Speicher passen.

## Beispielverwendung

Wir können die folgenden Testfälle verwenden, um unsere Lösung zu überprüfen:

- Wenn die Eingabe None ist, sollte die Funktion eine Ausnahme auslösen.
- Wenn das Element in der Matrix gefunden wird, sollte die Funktion seine Position als Tupel (Zeile, Spalte) zurückgeben.
- Wenn das Element in der Matrix nicht gefunden wird, sollte die Funktion None zurückgeben.
