# Clamp Number Challenge

## Problem

Schreibe eine Funktion `clamp_number(num, a, b)`, die drei Parameter annimmt:

- `num` (Integer oder Float): Die Zahl, die geklammert werden soll
- `a` (Integer oder Float): Die untere Grenze des Bereichs
- `b` (Integer oder Float): Die obere Grenze des Bereichs

Die Funktion sollte `num` innerhalb des eingeschlossenen Bereichs, der durch die Grenzwerte definiert ist, klammern. Wenn `num` innerhalb des Bereichs (`a`, `b`) liegt, gebe `num` zurück. Andernfalls gebe die nächste Zahl im Bereich zurück.

## Beispiel

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
clamp_number(10, 1, 5) # 5
clamp_number(-10, -5, -1) # -5
```
