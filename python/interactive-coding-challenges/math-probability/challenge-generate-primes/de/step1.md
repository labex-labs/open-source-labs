# Primzahlen generieren

## Problemstellung

Schreiben Sie eine Python-Funktion, die eine Liste von Primzahlen generiert. Die Funktion sollte eine ganze Zahl als Eingabe entgegennehmen und eine Liste von booleschen Werten zurückgeben, wobei jeder Wert angibt, ob der Index eine Primzahl ist oder nicht. Beispielsweise sollte bei einer Eingabe von 20 die Ausgabe [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True] sein, wobei der Wert an Index 2 True ist, da 2 eine Primzahl ist, und der Wert an Index 4 False ist, da 4 keine Primzahl ist.

## Anforderungen

- Die Funktion sollte 1 nicht als Primzahl betrachten.
- Die Funktion sollte ungültige Eingaben durch das Erhöhen einer Ausnahme behandeln.
- Die Funktion sollte die Liste der Primzahlen im Speicher generieren.

## Beispielverwendung

- Keine Eingabe -> Ausnahme
- Nicht eine Ganzzahl -> Ausnahme
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
