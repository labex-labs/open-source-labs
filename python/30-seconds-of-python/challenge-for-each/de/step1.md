# Führe Funktion für jedes Listelement aus

## Problem

Schreiben Sie eine Funktion `for_each(itr, fn)`, die eine Liste `itr` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `fn` einmal für jedes Element in `itr` ausführen.

## Beispiel

```python
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # druckt 1 4 9
```

Im obigen Beispiel wird die `for_each`-Funktion mit einer Liste `[1, 2, 3]` und einer Funktion `print_square` aufgerufen. Die `print_square`-Funktion wird einmal für jedes Element in der Liste ausgeführt und druckt das Quadrat jeder Zahl.
