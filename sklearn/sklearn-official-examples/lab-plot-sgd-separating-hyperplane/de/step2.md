# Trainieren des SVM-Modells mit SGD

Als nächstes müssen wir das SVM-Modell mit SGD trainieren. Wir werden die Klasse `SGDClassifier` aus Scikit-learn verwenden, um das Modell zu trainieren. Wir werden den Parameter `loss` auf "hinge" setzen, um den SVM-Algorithmus zu verwenden, und den Parameter `alpha` auf 0,01, um die Regularisierungstärke zu steuern. Wir werden auch den Parameter `max_iter` auf 200 setzen, um die Anzahl der Iterationen zu begrenzen.

```python
# fit the model
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
