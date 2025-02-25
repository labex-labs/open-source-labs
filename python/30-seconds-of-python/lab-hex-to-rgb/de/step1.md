# Hexadezimal zu RGB-Konvertierung

Schreiben Sie eine Funktion `hex_to_rgb(hex_code)`, die einen hexadezimalen Farbcode als Zeichenfolge akzeptiert und ein Tupel von ganzen Zahlen zurückgibt, die den RGB-Komponenten entsprechen. Die Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie eine List Comprehension in Kombination mit `int()` und der Listen-Slice-Notation, um die RGB-Komponenten aus der hexadezimalen Zeichenfolge zu erhalten.
2. Verwenden Sie `tuple()`, um die resultierende Liste in ein Tupel umzuwandeln.

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
