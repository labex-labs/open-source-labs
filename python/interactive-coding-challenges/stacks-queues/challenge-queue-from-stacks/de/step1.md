# Warteschlange aus Stapelstrukturen

## Problem

Das Implementieren einer Warteschlange mit zwei Stapelstrukturen kann ein herausforderndes Problem sein. Die Grundidee besteht darin, eine Stapelstruktur für die Einfügeoperationen und die andere Stapelstruktur für die Entnahmeoperationen zu verwenden. Wenn ein Element in die Warteschlange eingefügt wird, wird es auf die erste Stapelstruktur gelegt. Wenn ein Element aus der Warteschlange entfernt wird, wird es von der zweiten Stapelstruktur genommen. Wenn die zweite Stapelstruktur leer ist, nehmen wir alle Elemente von der ersten Stapelstruktur und legen sie in umgekehrter Reihenfolge auf die zweite Stapelstruktur. Dadurch wird sichergestellt, dass das erste eingefügte Element auch das erste entnommene Element ist.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Wir müssen zwei Methoden implementieren: Einfügen (enqueue) und Entnehmen (dequeue).
- Wir nehmen an, dass wir bereits eine Stapelstruktur-Klasse haben, die für dieses Problem verwendet werden kann.
- Wir dürfen keinen None-Wert auf den Stapel legen.
- Wir können annehmen, dass dieses Problem in den verfügbaren Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie wir unsere Implementierung einer Warteschlange mit zwei Stapelstrukturen verwenden können:

- Einfügen und Entnehmen von einer leeren Stapelstruktur: Wir können ein Element in die Warteschlange einfügen und dann entnehmen, um sicherzustellen, dass die Warteschlange richtig funktioniert.
- Einfügen und Entnehmen von einer nicht-leeren Stapelstruktur: Wir können mehrere Elemente in die Warteschlange einfügen und dann entnehmen, um sicherzustellen, dass die Warteschlange richtig funktioniert.
- Mehrere aufeinanderfolgende Einfügeoperationen: Wir können mehrere Elemente nacheinander in die Warteschlange einfügen und dann entnehmen, um sicherzustellen, dass die Warteschlange richtig funktioniert.
- Mehrere aufeinanderfolgende Entnahmeoperationen: Wir können mehrere Elemente in die Warteschlange einfügen und dann nacheinander entnehmen, um sicherzustellen, dass die Warteschlange richtig funktioniert.
- Einfügen nach einer Entnahme: Wir können ein Element in die Warteschlange einfügen, es entnehmen und dann ein weiteres Element in die Warteschlange einfügen, um sicherzustellen, dass die Warteschlange richtig funktioniert.
- Entnehmen nach einem Einfügen: Wir können ein Element in die Warteschlange einfügen, es entnehmen und dann ein weiteres Element in die Warteschlange einfügen, um sicherzustellen, dass die Warteschlange richtig funktioniert.
