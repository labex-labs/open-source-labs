# Partition

## Problem

Gegeben eine singuläre verkettete Liste, partitioniere sie um einen Wert x, sodass alle Knoten kleiner als x vor allen Knoten größer oder gleich x kommen. Die Funktion sollte eine neue verkettete Liste zurückgeben.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die verkettete Liste ist nicht-zirkulär und singulär verkettet.
- Die Funktion sollte eine neue verkettete Liste zurückgeben.
- Der Eingabewert x ist gültig.
- Wir haben bereits eine Klasse für verkettete Listen, die für dieses Problem verwendet werden kann.
- Wir können zusätzliche Datenstrukturen erstellen.
- Das Problem passt in den Arbeitsspeicher.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion funktionieren sollte:

- Leere Liste -> []
- Liste mit einem Element -> [Element]
- Linke verkettete Liste ist leer -> [10, 11, 12]
- Rechte verkettete Liste ist leer -> [1, 2, 3]
- Allgemeiner Fall
  - Partition = 10
  - Eingabe: 4, 3, 7, 8, 10, 1, 10, 12
  - Ausgabe: 4, 3, 7, 8, 1, 10, 10, 12
