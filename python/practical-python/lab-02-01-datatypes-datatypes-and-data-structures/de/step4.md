# Tupel

Ein Tupel ist eine Sammlung von Werten, die zusammen gruppiert sind.

Beispiel:

```python
s = ('GOOG', 100, 490.1)
```

Manchmal werden die `()` in der Syntax weggelassen.

```python
s = 'GOOG', 100, 490.1
```

Spezielle Fälle (0-Tupel, 1-Tupel).

```python
t = ()            # Ein leeres Tupel
w = ('GOOG', )    # Ein 1-Element-Tupel
```

Tupel werden oft verwendet, um einfache Datensätze oder Strukturen zu repräsentieren. Typischerweise ist es ein einzelnes Objekt mit mehreren Teilen. Ein gutes Analogie: _Ein Tupel ist wie eine einzelne Zeile in einer Datenbanktabelle._

Die Inhalte eines Tupels sind geordnet (wie ein Array).

```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

Die Inhalte können jedoch nicht geändert werden.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

Man kann jedoch ein neues Tupel basierend auf einem bestehenden Tupel erstellen.

```python
s = (s[0], 75, s[2])
```
