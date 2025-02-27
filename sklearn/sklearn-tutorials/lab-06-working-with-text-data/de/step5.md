# Auswerten des Modells

Um die Leistung unseres Modells zu evaluieren, können wir einen separaten Testdatensatz verwenden. Wir können den Testdatensatz mit dem gleichen Verfahren wie den Trainingsdatensatz laden.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

Jetzt können wir den Testdatensatz vorverarbeiten und die Merkmalsvektoren extrahieren.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

Schließlich können wir unser trainiertes Modell verwenden, um Vorhersagen für den Testdatensatz zu machen und die Genauigkeit zu berechnen.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
