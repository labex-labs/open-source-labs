# RGB in Hex umwandeln

Schreiben Sie eine Funktion `rgb_to_hex(r, g, b)`, die drei ganze Zahlen annimmt, die die Werte der roten, grünen und blauen Komponenten einer Farbe darstellen, und gibt einen String zurück, der den hexadezimalen Farbcode darstellt. Die Ausgabezeichenfolge sollte im Format `RRGGBB` vorliegen, wobei `RR`, `GG` und `BB` zwei-stellige hexadezimale Werte sind, die die roten, grünen und blauen Komponenten jeweils darstellen.

Beispielsweise sollte die Ausgabe für die Eingabewerte `255`, `165` und `1` der String `'FFA501'` sein.

```python
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
```

```python
rgb_to_hex(255, 165, 1) # 'FFA501'
```
