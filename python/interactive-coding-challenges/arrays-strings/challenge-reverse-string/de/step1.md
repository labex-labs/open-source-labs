# Zeichenkette umkehren

## Problem

Implementieren Sie eine Funktion, um eine Zeichenkette (eine Liste von Zeichen) in-place umzukehren. Dies bedeutet, dass die Funktion die ursprüngliche Zeichenkette modifizieren sollte, anstatt eine neue zu erstellen. Die Funktion sollte eine Liste von Zeichen als Eingabe entgegennehmen und die gleiche Liste mit den umgekehrten Zeichen zurückgeben.

Um dieses Problem zu lösen, müssen wir einige Anforderungen berücksichtigen:

## Anforderungen

- Es kann angenommen werden, dass die Zeichenkette ASCII ist.
- Da wir dies in-place tun müssen, können wir den Slicing-Operator oder die reversed-Funktion nicht verwenden.
- Da Python-Zeichenketten unveränderlich sind, können wir stattdessen eine Liste von Zeichen verwenden.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie die Funktion verhalten sollte:

- None -> None
- [''] -> ['']
- ['f', 'o', 'o','', 'b', 'a', 'r'] -> ['r', 'a', 'b','', 'o', 'o', 'f']
