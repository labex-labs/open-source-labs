# Merkmalsextraktion

Um die Text-Daten als Merkmalsvektoren zu repräsentieren, können wir die Bag-of-Words-Repräsentation verwenden. Diese Repräsentation weist jeder einzelnen Wörter im Trainingssatz eine feste ganzzahlige ID zu und zählt die Anzahl der Vorkommen jedes Worts in jedem Dokument. Wir können diese Merkmalsvektoren mit Hilfe von `CountVectorizer` aus scikit-learn extrahieren.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Extrahiere Merkmalsvektoren
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

Jetzt haben wir die Merkmalsvektoren extrahiert, und wir können sie verwenden, um unser Modell zu trainieren.
