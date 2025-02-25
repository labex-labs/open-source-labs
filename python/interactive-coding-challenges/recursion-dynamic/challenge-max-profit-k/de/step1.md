# Max Profit K

## Problem

Gegeben ist eine Liste von Aktienkursen an jedem aufeinanderfolgenden Tag. Bestimmen Sie die maximalen Gewinne bei k Transaktionen. Das Problem erfordert die Bestimmung des maximalen Gewinns, der aus einer Liste von Aktienkursen an aufeinanderfolgenden Tagen erzielt werden kann, unter Berücksichtigung von k Transaktionen. Die Transaktionen bestehen aus dem Kauf und Verkauf von Aktien, und die maximale Anzahl von Transaktionen ist auf k begrenzt. Die Lösung sollte den maximalen Gewinn und die Tage zum Kauf und Verkauf zurückgeben.

## Anforderungen

Um das Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- k repräsentiert die Anzahl der Verkaufstransaktionen.
- Die Eingabe von Preisen ist ein Array von ganzen Zahlen.
- Die Eingaben können ungültig sein.
- Wenn die Preise ständig abnehmen und es keine Möglichkeit gibt, einen Gewinn zu erzielen, sollte die Lösung 0 zurückgeben.
- Die Ausgabe sollte der maximale Gewinn und die Tage zum Kauf und Verkauf sein.
- Die Lösung sollte im Speicher passen.

## Beispielverwendung

Die folgenden Beispiele veranschaulichen die Verwendung der Lösung:

- Preise: None oder k: None -> None
- Preise: [] oder k <= 0 -> []
- Preise: [0, -1, -2, -3, -4, -5]
  - (maximaler Gewinn, Liste von Transaktionen)
  - (0, [])
- Preise: [2, 5, 7, 1, 4, 3, 1, 3] k: 3
  - (maximaler Gewinn, Liste von Transaktionen)
  - (10, [Type.SELL Tag: 7 Preis: 3,
    Type.BUY Tag: 6 Preis: 1,
    Type.SELL Tag: 4 Preis: 4,
    Type.BUY Tag: 3 Preis: 1,
    Type.SELL Tag: 2 Preis: 7,
    Type.BUY Tag: 0 Preis: 2])
