# Primzahl überprüfen

## Problemstellung

Schreiben Sie eine Python-Funktion, die eine ganze Zahl als Eingabe erhält und True zurückgibt, wenn die Zahl eine Primzahl ist, und False sonst. Wenn die Eingabe keine ganze Zahl ist oder kleiner als 2 ist, sollte die Funktion eine Ausnahme auslösen.

Eine Zahl wird als Primzahl angesehen, wenn sie nur durch 1 und sich selbst teilbar ist. Beispielsweise sind 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 und 97 die ersten 25 Primzahlen.

## Anforderungen

Das Programm sollte die folgenden Anforderungen erfüllen:

- Die Funktion sollte eine ganze Zahl als Eingabe akzeptieren.
- Wenn die Eingabe keine ganze Zahl ist oder kleiner als 2 ist, sollte die Funktion eine Ausnahme auslösen.
- Die Funktion sollte True zurückgeben, wenn die Eingabe eine Primzahl ist, und False sonst.
- Das Programm sollte 1 nicht als Primzahl betrachten.

## Beispielverwendung

- `check_prime(None)` -> `Ausnahme`
- `check_prime('hello')` -> `Ausnahme`
- `check_prime(1)` -> `False`
- `check_prime(7)` -> `True`
