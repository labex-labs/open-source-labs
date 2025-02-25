# Führe Funktion für jedes Listenelement in umgekehrter Reihenfolge aus

## Problem

Schreiben Sie eine Funktion `for_each_right(itr, fn)`, die eine Liste `itr` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `fn` einmal für jedes Element in `itr` ausführen, beginnend mit dem letzten.

## Beispiel

```python
for_each_right([1, 2, 3], print) # 3 2 1
```

## Beschränkungen

- Die Funktion sollte für jede Liste und Funktion funktionieren.
- Die Funktion sollte die ursprüngliche Liste nicht ändern.
