# Suche in einem verdrehten Array

## Problem

Gegeben ist ein sortiertes Array, das eine Anzahl von Malen verdreht wurde. Wir müssen ein bestimmtes Element im Array finden. Beispielsweise, wenn das ursprüngliche sortierte Array [1, 2, 3, 4, 5] war und es zweimal verdreht wurde, um [3, 4, 5, 1, 2] zu werden, müssen wir den Index eines bestimmten Elements, wie 4, finden.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die Eingabe ist ein Array von ganzen Zahlen.
- Wir wissen nicht, wie oft das Array verdreht wurde.
- Das Array war ursprünglich in aufsteigender Reihenfolge sortiert.
- Für die Ausgabe müssen wir den Index des Elements zurückgeben, nach dem wir suchen.
- Wir dürfen nicht annehmen, dass die Eingaben gültig sind.
- Wir können annehmen, dass die Lösung in den verfügbaren Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- Wenn keine Eingabe angegeben wird, sollte eine Ausnahme ausgelöst werden.
- Wenn ein leeres Array angegeben wird, sollte None zurückgegeben werden.
- Wenn das Element, nach dem wir suchen, im Array nicht gefunden wird, sollte None zurückgegeben werden.
- Wenn das Array Duplikate enthält, sollte die Funktion immer noch den richtigen Index finden können.
- Wenn das Array keine Duplikate enthält, sollte die Funktion immer noch den richtigen Index finden können.
