# Arbeiten mit Datentypen

NumPy-Datentypen werden als `dtype` (Data-Type)-Objekte dargestellt. Nachdem Sie NumPy mit `import numpy as np` importiert haben, können Sie die Datentypen über `np.bool_`, `np.float32` usw. zugreifen.

Sie können Datentypen als Funktionen verwenden, um Python-Zahlen in Array-Skalare zu konvertieren, Python-Zahlenfolgen in Arrays vom entsprechenden Typ oder als Argumente für das dtype-Schlüsselwort in vielen NumPy-Funktionen oder -Methoden. Hier sind einige Beispiele:

```python
x = np.float32(1.0)
# x ist jetzt ein float32-Array-Skalar mit dem Wert 1.0

y = np.int_([1,2,4])
# y ist jetzt ein int-Array mit den Werten [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z ist jetzt ein uint8-Array mit den Werten [0, 1, 2]
```

Sie können auch auf Arraytypen über Zeichencodes verweisen, obwohl es empfohlen wird, stattdessen dtype-Objekte zu verwenden. Beispielsweise:

```python
np.array([1, 2, 3], dtype='f')
# gibt ein Array mit den Werten [1., 2., 3.] und dtype float32 zurück
```

Um den Typ eines Arrays umzuwandeln, können Sie die `.astype()`-Methode oder den Typ selbst als Funktion verwenden. Beispielsweise:

```python
z.astype(float)
# gibt das Array z mit dtype float64 zurück

np.int8(z)
# gibt das Array z mit dtype int8 zurück
```
