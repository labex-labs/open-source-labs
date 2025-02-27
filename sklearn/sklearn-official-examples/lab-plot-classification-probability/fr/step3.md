# Définir les classifieurs

Nous définissons différents classifieurs pour l'ensemble de données.

```python
C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # pour GPC

# Créer différents classifieurs.
classifiers = {
    "Logistique L1": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "Logistique L2 (Multinomiale)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "Logistique L2 (OvR)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    ),
    "SVC linéaire": SVC(kernel="linear", C=C, probability=True, random_state=0),
    "GPC": GaussianProcessClassifier(kernel),
}
```
