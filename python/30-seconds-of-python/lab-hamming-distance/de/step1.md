# Hamming-Distanz

Schreiben Sie eine Funktion `hamming_distance(a, b)`, die zwei ganze Zahlen als Argumente nimmt und die Hamming-Distanz zwischen ihnen zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie den XOR-Operator (`^`), um die Bitunterschiede zwischen den beiden Zahlen zu finden.
2. Verwenden Sie `bin()`, um das Ergebnis in einen Binärstring umzuwandeln.
3. Konvertieren Sie den String in eine Liste und verwenden Sie die `count()`-Methode der `str`-Klasse, um die Anzahl der `1` darin zu zählen und zurückzugeben.

```python
def hamming_distance(a, b):
  return bin(a ^ b).count('1')
```

```python
hamming_distance(2, 3) # 1
```
