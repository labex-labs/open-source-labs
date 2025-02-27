# Definiere die Klassifizierer

Wir definieren verschiedene Klassifizierer für den Datensatz.

```python
C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # für GPC

# Erstelle verschiedene Klassifizierer.
classifiers = {
    "L1 logistische Regression": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 logistische Regression (Multinomial)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 logistische Regression (OvR)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    ),
    "Linear SVC": SVC(kernel="linear", C=C, probability=True, random_state=0),
    "GPC": GaussianProcessClassifier(kernel),
}
```
