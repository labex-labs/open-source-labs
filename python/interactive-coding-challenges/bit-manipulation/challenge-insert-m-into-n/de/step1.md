# M in N einfügen

## Problem

Gegeben zwei 16-Bit-Zahlen, `n` und `m`, und zwei Indizes `i` und `j`, füge `m` in `n` ein, sodass `m` am Bit `j` beginnt und am Bit `i` endet. Das Programm sollte die folgenden Fälle behandeln:

- Wenn keine Eingabe gegeben ist, sollte eine Ausnahme ausgelöst werden.
- Wenn ein negativer Index für `i` oder `j` gegeben ist, sollte eine Ausnahme ausgelöst werden.
- Wenn die Eingaben ungültig sind, sollte eine Ausnahme ausgelöst werden.
- Wenn `i` bis `j` nicht genug Platz für `m` haben, sollte eine Ausnahme ausgelöst werden.

Das Programm sollte die resultierende 16-Bit-Zahl nach der Einfügung zurückgeben.

## Anforderungen

Das Programm sollte die folgenden Anforderungen erfüllen:

- `j` sollte größer als `i` sein.
- `i` bis `j` sollten genug Platz für `m` haben.
- Die Eingaben sollten gültig sein.
- Das Programm sollte in den Arbeitsspeicher passen.

## Beispielverwendung

Hier ist ein Beispiel für die Verwendung des Programms:

```txt
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100
```

In diesem Beispiel wird `m` in `n` eingefügt, sodass `m` am Bit `j=6` beginnt und am Bit `i=2` endet. Die resultierende 16-Bit-Zahl ist `0000 0100 0100 1100`.
