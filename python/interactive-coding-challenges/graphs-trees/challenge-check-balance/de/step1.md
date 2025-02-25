# Überprüfe die Balance

## Problem

Gegeben einen Binärbaum, schreiben Sie eine Python-Funktion, um zu bestimmen, ob er balanciert ist. Ein Binärbaum wird als balanciert betrachtet, wenn die Höhen der beiden Teilbäume eines beliebigen Knotens um höchstens eins voneinander abweichen. Die Funktion sollte die Wurzelknoten des Binärbaums als Eingabe entgegennehmen und True zurückgeben, wenn der Baum balanciert ist, und False sonst. Wenn die Eingabe None ist, sollte die Funktion eine Ausnahme auslösen.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen erfüllen:

- Ein balancierter Baum ist einer, bei dem die Höhen der beiden Teilbäume eines beliebigen Knotens um nicht mehr als 1 voneinander abweichen.
- Wenn die Eingabe None ist, sollte die Funktion eine Ausnahme auslösen.
- Wir können davon ausgehen, dass wir bereits eine Node-Klasse mit einer insert-Methode haben.
- Wir können davon ausgehen, dass das Programm in den Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie die Funktion verhalten sollte:

- None -> Ausnahme auslösen
- 1 -> True
- 5, 3, 8, 1, 4 -> True
- 5, 3, 8, 9, 10 -> False
