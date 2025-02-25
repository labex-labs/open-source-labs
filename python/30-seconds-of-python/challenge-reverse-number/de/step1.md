# Umkehrzahl-Herausforderung

## Problemstellung

Schreibe eine Funktion `reverse_number(n)`, die eine Zahl als Argument entgegennimmt und die umgekehrte Zahl zurückgibt. Die Funktion sollte die folgenden Anforderungen erfüllen:

- Die Funktion sollte die Zahl umkehren, unabhängig davon, ob sie positiv oder negativ ist.
- Die Funktion sollte eine Gleitkommazahl zurückgeben, wenn die Eingabe eine Gleitkommazahl ist, und eine Ganzzahl, wenn die Eingabe eine Ganzzahl ist.
- Die Funktion darf keine eingebauten Funktionen verwenden, die direkt eine Zahl umkehren (z.B. `reversed()`).
- Die Funktion darf keine eingebauten Funktionen verwenden, die direkt eine Zahl in einen String umwandeln (z.B. `str()`).
- Die Funktion darf keine eingebauten Funktionen verwenden, die direkt einen String in eine Zahl umwandeln (z.B. `int()` oder `float()`).

## Beispiel

```python
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```
