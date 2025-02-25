# Bst

## Problem

Ein binärer Suchbaum ist eine Datenstruktur, die schnelle Such-, Einfüge- und Löschoperationen ermöglicht. Es ist ein Baum, in dem jeder Knoten maximal zwei Kinder hat, und das linke Kind ist kleiner als der Elternknoten, und das rechte Kind ist größer als der Elternknoten. Die Einfüge-Methode fügt einen neuen Knoten in den Baum an der passenden Position basierend auf seinem Wert hinzu.

Ihre Aufgabe ist es, einen binären Suchbaum mit einer Einfüge-Methode in Python zu implementieren. Die Einfüge-Methode sollte einen Wert entgegennehmen und einen neuen Knoten in den Baum an der passenden Position basierend auf seinem Wert hinzufügen. Wenn die Wurzeleingabe None ist, soll ein Baum zurückgegeben werden, dessen einziges Element der neue Wurzelknoten ist.

## Anforderungen

Um diese Aufgabe zu lösen, müssen Sie die folgenden Anforderungen erfüllen:

- Sie können keine None-Werte einfügen.
- Sie können davon ausgehen, dass Sie mit gültigen ganzen Zahlen arbeiten.
- Sie können davon ausgehen, dass alle linken Nachkommen kleiner oder gleich dem Knoten sind und alle rechten Nachkommen größer als der Knoten sind.
- Sie müssen nicht die Elternknoten verfolgen, aber das ist optional.
- Sie können davon ausgehen, dass dies in den Speicher passt.

## Beispielverwendung

### Einfügen

Die Einfügung wird durch die folgende Traversierung getestet:

### In-Order Traversierung

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

Sie müssen die In-Order-Traversierung nicht implementieren, sie ist Teil der Unit-Tests.
