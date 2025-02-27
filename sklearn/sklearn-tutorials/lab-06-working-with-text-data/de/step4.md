# Training des Modells

Jetzt, nachdem wir unsere Merkmalsvektoren haben, können wir ein Modell trainieren, um die Text-Daten zu klassifizieren. In diesem Beispiel werden wir den Multinomial Naive Bayes-Algorithmus verwenden, der ein populärer Algorithmus für die Textklassifizierung ist.

```python
from sklearn.naive_bayes import MultinomialNB

# Trainiere das Modell
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

Jetzt ist unser Modell trainiert und bereit für Vorhersagen.
