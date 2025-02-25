# Palindrom

## Problem

Gegeben eine singuläre verkettete Liste, bestimmen Sie, ob es sich um ein Palindrom handelt. Eine verkettete Liste ist ein Palindrom, wenn die Reihenfolge der Elemente in der Liste sowohl von vorne nach hinten als auch von hinten nach vorne gleich ist.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die verkettete Liste ist nicht zirkulär und singulär verknüpft.
- Ein einzelnes Zeichen oder eine einzelne Zahl wird nicht als Palindrom betrachtet.
- Wir haben bereits eine Klasse für verkettete Listen, die für dieses Problem verwendet werden kann.
- Wir können zusätzliche Datenstrukturen verwenden.
- Die verkettete Liste passt in den Arbeitsspeicher.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verhalten sollte:

- Eine leere Liste sollte False zurückgeben.
- Eine Liste mit einem einzelnen Element sollte False zurückgeben.
- Eine Liste mit zwei oder mehr Elementen, die kein Palindrom ist, sollte False zurückgeben.
- Ein Palindrom mit einer geraden Länge sollte True zurückgeben.
- Ein Palindrom mit einer ungeraden Länge sollte True zurückgeben.
