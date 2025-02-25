# Verkettete Liste

## Problem

Implementiere eine verkettete Liste mit folgenden Methoden:

- insert(value): Fügt einen neuen Knoten mit dem angegebenen Wert am Anfang der Liste ein.
- append(value): Fügt einen neuen Knoten mit dem angegebenen Wert am Ende der Liste ein.
- find(value): Gibt den ersten Knoten in der Liste mit dem angegebenen Wert zurück, oder None, wenn kein solcher Knoten existiert.
- delete(value): Entfernt den ersten Knoten in der Liste mit dem angegebenen Wert, oder tut nichts, wenn kein solcher Knoten existiert.
- length(): Gibt die Anzahl der Knoten in der Liste zurück.
- print(): Gibt die Werte aller Knoten in der Liste getrennt durch Leerzeichen aus.

## Anforderungen

Die Implementierung der verketteten Liste sollte folgende Anforderungen erfüllen:

- Die verkettete Liste ist nicht-zirkulär und einfach verkettet.
- Die Implementierung verfolgt nur den Kopf der Liste, nicht den Schwanz.
- None-Werte können nicht in die Liste eingefügt werden.

## Beispielverwendung

### Einfügen am Anfang

- Ein None einfügen: Wirft einen Fehler, da None-Werte nicht in die Liste eingefügt werden können.
- In eine leere Liste einfügen: Fügt den Wert als ersten Knoten in die Liste ein.
- In eine Liste mit einem oder mehr Elementen einfügen: Fügt den Wert als ersten Knoten in die Liste ein und verschiebt die vorhandenen Knoten nach rechts.

### Anhängen

- Ein None anhängen: Wirft einen Fehler, da None-Werte nicht in die Liste eingefügt werden können.
- In eine leere Liste anhängen: Fügt den Wert als ersten Knoten in die Liste ein.
- In eine Liste mit einem oder mehr Elementen anhängen: Fügt den Wert als letzten Knoten in die Liste ein und aktualisiert die Referenz des vorherigen letzten Knotens, um auf den neuen Knoten zu verweisen.

### Suchen

- Ein None suchen: Gibt None zurück, da None-Werte in der Liste nicht gefunden werden können.
- In einer leeren Liste suchen: Gibt None zurück, da es keine Knoten in der Liste gibt.
- In einer Liste mit einem oder mehr übereinstimmenden Elementen suchen: Gibt den ersten Knoten in der Liste mit dem angegebenen Wert zurück.
- In einer Liste ohne Übereinstimmungen suchen: Gibt None zurück, da es keine Knoten in der Liste mit dem angegebenen Wert gibt.

### Löschen

- Ein None löschen: Tut nichts, da None-Werte nicht aus der Liste gelöscht werden können.
- In einer leeren Liste löschen: Tut nichts, da es keine Knoten in der Liste gibt.
- In einer Liste mit einem oder mehr übereinstimmenden Elementen löschen: Entfernt den ersten Knoten in der Liste mit dem angegebenen Wert und verschiebt die vorhandenen Knoten nach links.
- In einer Liste ohne Übereinstimmungen löschen: Tut nichts, da es keine Knoten in der Liste mit dem angegebenen Wert gibt.

### Länge

- Länge von null oder mehr Elementen: Gibt die Anzahl der Knoten in der Liste zurück.

### Drucken

- Eine leere Liste drucken: Gibt nichts aus.
- Eine Liste mit einem oder mehr Elementen drucken: Gibt die Werte aller Knoten in der Liste getrennt durch Leerzeichen aus.
