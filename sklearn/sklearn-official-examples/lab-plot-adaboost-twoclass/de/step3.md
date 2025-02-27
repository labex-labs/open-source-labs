# Erstellen und Anpassen eines AdaBoost-verstärkten Entscheidungsbaums

In diesem Schritt erstellen wir einen AdaBoost-verstärkten Entscheidungsbaum mithilfe der Klasse `AdaBoostClassifier` aus dem Modul `sklearn.ensemble`. Wir verwenden den Entscheidungsbaum als Basisestimator und setzen den Parameter `max_depth` auf 1. Wir setzen auch den Parameter `algorithm` auf "SAMME" und den Parameter `n_estimators` auf 200. Schließlich passen wir den Klassifizierer an den Datensatz an.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
