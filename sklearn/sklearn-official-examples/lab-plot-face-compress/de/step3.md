# Arbeitsspeicherbedarf

Wir werden nun den Arbeitsspeicherbedarf der komprimierten Bilder überprüfen. Wir erwarten, dass das komprimierte Bild 8-mal weniger Arbeitsspeicher benötigt als das Originalbild.

```python
print(f"Die Anzahl der in RAM verwendeten Bytes beträgt {compressed_raccoon_kmeans.nbytes}")
print(f"Kompressionsverhältnis: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
