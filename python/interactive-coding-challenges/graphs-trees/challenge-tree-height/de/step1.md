# Baumhöhe

## Problem

Gegeben einen binären Baum, schreiben Sie eine Python-Funktion, um die Höhe des Baums zu bestimmen. Die Höhe eines binären Baums ist die Länge des längsten Pfads vom Wurzelknoten zu irgendeinem Blattknoten im Baum.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen erfüllen:

- Der gegebene Baum ist ein binärer Baum.
- Wir haben bereits eine Node-Klasse mit einer insert-Methode.
- Die Lösung passt in den Speicher.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verhalten sollte:

- Wenn der Baum nur einen Knoten hat, ist die Höhe 1. Beispielsweise sollte die Ausgabe 1 sein, wenn die Eingabe 5 -> 1 ist.
- Wenn der Baum mehrere Knoten hat, ist die Höhe die Länge des längsten Pfads vom Wurzelknoten zu irgendeinem Blattknoten. Beispielsweise sollte die Ausgabe 3 sein, wenn die Eingabe 5, 2, 8, 1, 3 -> 3 ist.
