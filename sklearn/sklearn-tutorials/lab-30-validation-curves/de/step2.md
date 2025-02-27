# Mischen Sie die Daten

Um die Zufälligkeit in unserer Analyse zu gewährleisten, mischen wir die Reihenfolge der Proben in unserem Datensatz.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
