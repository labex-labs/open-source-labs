# Anpassen des gewichteten Modells

Wir trainieren ein gewichtetes Modell mit dem gleichen Algorithmus wie in Schritt 4, aber diesmal übergeben wir das sample_weight-Argument an die fit-Methode. Anschließend zeichnen wir die Entscheidungsfunktion des gewichteten Modells.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
