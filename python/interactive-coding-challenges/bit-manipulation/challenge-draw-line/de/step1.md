# Linie zeichnen

## Problem

Implementieren Sie die Methode `draw_line(screen, width, x1, x2)`, wobei `screen` eine Liste von Bytes ist, `width` durch 8 teilbar ist und `x1`, `x2` absolute Pixelpositionen sind. Die Methode sollte die entsprechenden Bits in `screen` setzen, um eine Linie von `x1` bis `x2` zu zeichnen.

### Anforderungen

Die Implementierung von `draw_line` muss die folgenden Anforderungen erfüllen:

- Es darf nicht angenommen werden, dass die Eingaben gültig sind.
- Die entsprechenden Bits in `screen` müssen gesetzt werden, um die Linie zu zeichnen.
- Es kann angenommen werden, dass die Implementierung in den Speicher passt.

## Beispielverwendung

Die folgenden Beispiele veranschaulichen das erwartete Verhalten von `draw_line`:

- Ungültige Eingaben -> Exception
  - `screen` ist leer
  - `width` = 0
  - irgendein Eingabeparameter ist `None`
  - `x1` oder `x2` ist außerhalb der Grenzen
- Allgemeiner Fall für `len(screen)` = 20, `width` = 32:
  - `x1` = 2, `x2` = 6
    - `screen[0]` = `int('00111110', base=2)`
  - `x1` = 68, `x2` = 80
    - `screen[8]`, `int('00001111', base=2)`
    - `screen[9]`, `int('11111111', base=2)`
    - `screen[10]`, `int('10000000', base=2)`
