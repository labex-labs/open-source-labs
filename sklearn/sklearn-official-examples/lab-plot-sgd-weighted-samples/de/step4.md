# Anpassen des ungewichteten Modells

Wir trainieren ein ungewichtetes Modell mit dem SGDClassifier-Algorithmus aus der scikit-learn-Bibliothek. Anschließend zeichnen wir die Entscheidungsfunktion des ungewichteten Modells.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
