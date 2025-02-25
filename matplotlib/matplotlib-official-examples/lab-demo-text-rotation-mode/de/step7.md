# Erstelle die Subfiguren und rufe die `test_rotation_mode`-Funktion auf

Wir werden zwei Subfiguren erstellen und die `test_rotation_mode`-Funktion mit den Parametern `fig` und `mode` aufrufen.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
