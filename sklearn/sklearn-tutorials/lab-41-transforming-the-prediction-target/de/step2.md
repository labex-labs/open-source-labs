# Mehrfachlabel-Binarisierung

Mehrfachlabel-Binarisierung ist der Prozess der Konvertierung einer Sammlung von Label-Sammlungen in ein Indikatorformat. Dies kann mit der Klasse `MultiLabelBinarizer` erreicht werden.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Definieren einer Liste von Label-Sammlungen
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Erstellen einer MultiLabelBinarizer-Instanz und Anwenden von fit_transform auf die Liste der Sammlungen
MultiLabelBinarizer().fit_transform(y)
```
