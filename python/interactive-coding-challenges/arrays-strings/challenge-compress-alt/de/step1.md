# Komprimieren Alternative

## Problem

Gegeben einen String, komprimieren Sie ihn so, dass aufeinanderfolgende Vorkommen desselben Zeichens durch das Zeichen gefolgt von der Anzahl der Vorkommen ersetzt werden. Beispielsweise würde der String 'AAABCCDDDD' zu 'A3BCCD4' werden. Wenn die komprimierte Zeichenkette jedoch nicht kürzer als die ursprüngliche Zeichenkette ist, geben Sie die ursprüngliche Zeichenkette zurück.

## Anforderungen

Um diese Herausforderung zu lösen, müssen die folgenden Anforderungen erfüllt werden:

- Der String wird als ASCII angenommen.
- Die Komprimierung ist case-sensitiv.
- Zusätzliche Datenstrukturen können verwendet werden.
- Es wird angenommen, dass der String in den Arbeitsspeicher passt.

## Beispielverwendung

Die folgenden sind Beispiele dafür, wie diese Funktion verwendet werden kann:

- `compress(None)` gibt `None` zurück
- `compress('')` gibt `''` zurück
- `compress('AABBCC')` gibt `'AABBCC'` zurück
- `compress('AAABCCDDDD')` gibt `'A3BCCD4'` zurück
