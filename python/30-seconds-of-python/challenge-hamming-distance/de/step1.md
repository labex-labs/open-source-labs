# Hamming-Distanz-Herausforderung

## Problem

Schreiben Sie eine Funktion `hamming_distance(a, b)`, die zwei Integer als Argumente nimmt und die Hamming-Distanz zwischen ihnen zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie den XOR-Operator (`^`), um die Bitunterschiede zwischen den beiden Zahlen zu finden.
2. Verwenden Sie `bin()`, um das Ergebnis in einen Binärstring umzuwandeln.
3. Konvertieren Sie den String in eine Liste und verwenden Sie die `count()`-Methode der `str`-Klasse, um die Anzahl der `1` darin zu zählen und zurückzugeben.

## Beispiel

```python
hamming_distance(2, 3) # 1
hamming_distance(10, 4) # 2
hamming_distance(0, 255) # 8
```
