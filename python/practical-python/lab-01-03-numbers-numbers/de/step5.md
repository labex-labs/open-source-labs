# Vergleiche

Die folgenden Vergleichs-/Relationsoperatoren funktionieren mit Zahlen:

    x < y      Kleiner als
    x <= y     Kleiner als oder gleich
    x > y      Größer als
    x >= y     Größer als oder gleich
    x == y     Gleich
    x!= y     Ungleich

Sie können komplexere boolesche Ausdrücke bilden, indem Sie

`and`, `or`, `not`

Verwenden. Hier sind ein paar Beispiele:

```python
if b >= a and b <= c:
    print('b ist zwischen a und c')

if not (b < a or b > c):
    print('b ist immer noch zwischen a und c')
```
