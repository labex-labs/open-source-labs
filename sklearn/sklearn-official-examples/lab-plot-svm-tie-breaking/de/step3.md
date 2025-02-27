# Erstellen von SVM-Modellen mit und ohne Tie-Breaking

In diesem Schritt erstellen wir zwei SVM-Modelle - eines mit deaktiviertem Tie-Breaking und eines mit aktiviertem Tie-Breaking. Wir verwenden die Klasse `SVC` aus scikit-learn, um diese Modelle zu erstellen. Der Parameter `break_ties` wird für die beiden Modelle auf `False` und `True` festgelegt.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```
