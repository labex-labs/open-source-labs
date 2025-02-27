# Verifikation

Um die Korrektheit der inversen Transformation zu verifizieren, können wir die ursprünglichen Daten `X` mit dem Ergebnis der inversen Transformation vergleichen.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

Hier wenden wir die Transformation auf die invers transformierten Daten `X_new_inversed` an und überprüfen, ob sie mit den ursprünglichen projizierten Daten `X_new` übereinstimmen, indem wir die Funktion `np.allclose` verwenden.
