# Slicing

Slicing bedeutet, eine Teilfolge aus einer Sequenz zu extrahieren. Die Syntax lautet `s[start:end]`. Dabei sind `start` und `end` die Indizes der Teilfolge, die Sie möchten.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

- Die Indizes `start` und `end` müssen ganze Zahlen sein.
- Slices enthalten den Endwert _nicht_. Es ist wie ein halboffenes Intervall aus der Mathematik.
- Wenn die Indizes weggelassen werden, nehmen sie standardmäßig den Anfang oder das Ende der Liste an.
