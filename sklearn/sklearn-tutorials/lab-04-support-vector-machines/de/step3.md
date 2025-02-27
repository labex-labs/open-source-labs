# Scores und Wahrscheinlichkeiten

- SVMs liefern keine direkten Wahrscheinlichkeitsschätzungen, aber Sie können die Wahrscheinlichkeitsschätzung aktivieren, indem Sie den Parameter `probability` auf `True` setzen:

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- Anschließend können Sie die Methode `predict_proba` verwenden, um die Wahrscheinlichkeiten für jede Klasse zu erhalten:

```python
clf.predict_proba([[2., 2.]])
```

- Beachten Sie, dass die Wahrscheinlichkeitsschätzung aufwendig ist und eine Kreuzvalidierung erfordert, also verwenden Sie sie mit Bedacht.
