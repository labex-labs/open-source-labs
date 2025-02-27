# Vorverarbeiten der Text-Daten

Bevor wir die Text-Daten für das maschinelle Lernen verwenden können, müssen wir sie vorverarbeiten. Dies umfasst mehrere Schritte, wie das Entfernen von Satzzeichen, das Konvertieren aller Texte in Kleinbuchstaben und das Tokenisieren des Texts in einzelne Wörter. Wir können diese Vorverarbeitungsschritte mit Hilfe von `CountVectorizer` und `TfidfTransformer` aus scikit-learn ausführen.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Vorverarbeiten der Text-Daten
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

Jetzt sind unsere Text-Daten vorverarbeitet und bereit für die Merkmalsextraktion.
