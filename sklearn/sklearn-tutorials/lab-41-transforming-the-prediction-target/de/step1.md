# Label-Binarisierung

Label-Binarisierung ist der Prozess der Konvertierung von Mehrklassen-Labels in eine binäre Indikator-Matrix. Dies kann mit der Klasse `LabelBinarizer` erreicht werden.

```python
from sklearn import preprocessing

# Erstellen einer LabelBinarizer-Instanz
lb = preprocessing.LabelBinarizer()

# Anpassen der LabelBinarizer an eine Liste von Mehrklassen-Labels
lb.fit([1, 2, 6, 4, 2])

# Die von der LabelBinarizer gelernten Klassen abrufen
lb.classes_

# Transformieren einer Liste von Mehrklassen-Labels in eine binäre Indikator-Matrix
lb.transform([1, 6])
```
