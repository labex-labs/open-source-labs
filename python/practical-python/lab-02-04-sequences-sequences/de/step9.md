# enumerate()-Funktion

Die `enumerate`-Funktion fügt einen zusätzlichen Zählerwert zur Iteration hinzu.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Schleifen mit i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

Die allgemeine Form lautet `enumerate(sequence [, start = 0])`. `start` ist optional. Ein gutes Beispiel für die Verwendung von `enumerate()` ist das Verfolgen der Zeilennummern beim Lesen einer Datei:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
     ...
```

Am Ende ist `enumerate` einfach eine schöne Abkürzung für:

```python
i = 0
for x in s:
    statements
    i += 1
```

Das Verwenden von `enumerate` erfordert weniger Tipparbeit und läuft etwas schneller.
