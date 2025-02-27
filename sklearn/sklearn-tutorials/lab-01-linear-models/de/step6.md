# Perzeptron

Das Perzeptron ist ein einfaches lineares Klassifizierungsalgorithmus, der für das大规模学习geeignet ist. Es aktualisiert sein Modell nur bei Fehlern, was es schneller zu trainieren macht als der stochastic gradient descent (SGD) mit Hinge - Verlust. Die resultierenden Modelle sind auch spärlicher.

Lassen Sie uns ein Perzeptronmodell anpassen.

```python
clf = linear_model.Perceptron(alpha=0.1)
clf.fit(X, y)

print(clf.coef_)
```

- Wir erstellen eine Instanz von `Perceptron` mit dem Regularisierungsparameter `alpha` auf 0,1 gesetzt.
- Wir verwenden die `fit`-Methode, um das Modell an die Trainingsdaten anzupassen.
- Wir drucken die Koeffizienten des Perzeptronmodells.
