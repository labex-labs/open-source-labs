# Listeniteration und -suche

Verwenden Sie `for`, um über die Inhalte der Liste zu iterieren.

```python
for name in names:
    # Verwenden Sie name
    # z.B. print(name)
  ...
```

Dies ähnelt einem `foreach`-Statement in anderen Programmiersprachen.

Um die Position eines Elements schnell zu finden, verwenden Sie `index()`.

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

Wenn das Element mehrmals vorhanden ist, gibt `index()` den Index des ersten Vorkommens zurück.

Wenn das Element nicht gefunden wird, wird eine `ValueError`-Ausnahme ausgelöst.
