# Zahl einschränken

Schreibe eine Funktion `clamp_number(num, a, b)`, die drei Parameter annimmt:

- `num` (Integer oder Float): Die zu clampende Zahl
- `a` (Integer oder Float): Die untere Grenze des Bereichs
- `b` (Integer oder Float): Die obere Grenze des Bereichs

Die Funktion sollte `num` innerhalb des durch die Grenzwerte angegebenen abgeschlossenen Bereichs einschränken. Wenn `num` innerhalb des Bereichs (`a`, `b`) liegt, gebe `num` zurück. Andernfalls gebe die nächste Zahl im Bereich zurück.

```python
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))
```

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```
