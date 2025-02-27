# Vorhersage der Klasswahrscheinlichkeiten für alle Klassifizierer

Wir werden die Klasswahrscheinlichkeiten für alle Klassifizierer mithilfe der predict_proba()-Funktion vorhersagen.

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
