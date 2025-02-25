# Entferne Mitte

## Problem

Gegeben eine nicht-zirkuläre, einfach verkettete Liste, entferne einen Knoten in der Mitte der Liste, wenn nur auf diesen Knoten zugegriffen werden kann. Wenn der letzte Knoten gelöscht wird, mache es zu einem Dummy mit dem Wert None. Du kannst davon ausgehen, dass wir bereits eine verkettete Listenklasse haben, die für dieses Problem verwendet werden kann.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die verkettete Liste ist nicht-zirkulär und einfach verkettet.
- Wenn der letzte Knoten gelöscht wird, mache es zu einem Dummy mit dem Wert None.
- Wir haben bereits eine verkettete Listenklasse, die für dieses Problem verwendet werden kann.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- Beim Löschen einer leeren Liste sollte None zurückgegeben werden.
- Beim Löschen von None sollte None zurückgegeben werden.
- Beim Löschen einer Liste mit einem Knoten sollte [None] zurückgegeben werden.
- Beim Löschen einer Liste mit mehreren Knoten sollte die aktualisierte Liste mit dem gelöschten Knoten zurückgegeben werden.
