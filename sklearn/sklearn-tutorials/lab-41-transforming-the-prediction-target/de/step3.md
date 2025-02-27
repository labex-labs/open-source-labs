# Label-Kodierung

Label-Kodierung ist der Prozess der Konvertierung von nicht numerischen Labels in numerische Labels. Dies kann mit der Klasse `LabelEncoder` erreicht werden.

```python
from sklearn import preprocessing

# Erstellen einer LabelEncoder-Instanz
le = preprocessing.LabelEncoder()

# Anpassen der LabelEncoder an eine Liste von nicht numerischen Labels
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# Die von der LabelEncoder gelernten Klassen abrufen
list(le.classes_)

# Transformieren einer Liste von nicht numerischen Labels in numerische Labels
le.transform(["tokyo", "tokyo", "paris"])

# Inverse Transformation numerischer Labels zurück in nicht numerische Labels
list(le.inverse_transform([2, 2, 1]))
```
