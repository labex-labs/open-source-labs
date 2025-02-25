# Hexadezimal zu RGB-Konvertierung

## Problemstellung

Schreiben Sie eine Funktion `hex_to_rgb(hex_code)`, die einen hexadezimalen Farbcode als Zeichenfolge entgegennimmt und ein Tupel von ganzen Zahlen zurückgibt, die den RGB-Komponenten entsprechen. Die Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie eine Listenkomprehension in Verbindung mit `int()` und der Listenausschnittsnotation, um die RGB-Komponenten aus der hexadezimalen Zeichenfolge zu erhalten.
2. Verwenden Sie `tuple()`, um die resultierende Liste in ein Tupel zu konvertieren.

## Beispiel

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
