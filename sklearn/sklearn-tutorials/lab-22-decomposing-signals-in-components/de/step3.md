# Nicht-negative Matrixfaktorisierung (NMF)

#### NMF mit der Frobenius-Norm

Die Nicht-negative Matrixfaktorisierung (NMF) ist eine alternative Methode zur Zerlegung, die von nicht-negativen Daten und Komponenten ausgeht. Sie findet eine Zerlegung der Daten in zwei Matrizen aus nicht-negativen Elementen, indem sie die Distanz zwischen den Daten und dem Matrizenprodukt der beiden Matrizen optimiert. Die NMF kann mit der Klasse `NMF` aus scikit-learn implementiert werden.

```python
from sklearn.decomposition import NMF

# Erstellen eines NMF-Objekts mit n_components als Anzahl der gewünschten Komponenten
nmf = NMF(n_components=2)

# Anpassen des NMF-Modells an die Daten
nmf.fit(data)

# Zerlegen der Daten in die zwei nicht-negativen Matrizen
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```
