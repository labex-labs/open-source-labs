# Ktes Element von der Letzten Stelle

## Problemstellung

Gegeben ist eine nicht-zirkuläre, singulär verkettete Liste. Die Aufgabe besteht darin, das k-te Element von der letzten Stelle in der Liste zu finden. Wenn k gleich 0 ist, sollte das letzte Element zurückgegeben werden. Wenn k größer als oder gleich der Länge der verketteten Liste ist, sollte None zurückgegeben werden. Es dürfen keine zusätzlichen Datenstrukturen verwendet werden, und es wird angenommen, dass eine Klasse für verkettete Listen bereits vorhanden ist.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Die verkettete Liste ist nicht-zirkulär und singulär verkettet.
- k ist eine gültige Ganzzahl.
- Wenn k gleich 0 ist, sollte das letzte Element zurückgegeben werden.
- Wenn k größer als oder gleich der Länge der verketteten Liste ist, sollte None zurückgegeben werden.
- Es dürfen keine zusätzlichen Datenstrukturen verwendet werden.
- Eine Klasse für verkettete Listen ist bereits vorhanden.

## Beispielverwendung

Die folgenden Szenarien können verwendet werden, um die Lösung zu testen:

- Eine leere Liste sollte None zurückgeben.
- Wenn k größer als oder gleich der Länge der verketteten Liste ist, sollte None zurückgegeben werden.
- Wenn die verkettete Liste nur ein Element hat und k gleich 0 ist, sollte das Element zurückgegeben werden.
- Für einen allgemeinen Fall mit vielen Elementen, wobei k kleiner als die Länge der verketteten Liste ist, sollte das k-te Element von der letzten Stelle zurückgegeben werden.
