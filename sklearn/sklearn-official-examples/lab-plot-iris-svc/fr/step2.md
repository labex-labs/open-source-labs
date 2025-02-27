# Créez des classifieurs SVM et ajustez les données

```python
C = 1.0  # Paramètre de régularisation SVM
models = (
    svm.SVC(kernel="linéaire", C=C),
    svm.LinearSVC(C=C, max_iter=10000, dual="auto"),
    svm.SVC(kernel="rbf", gamma=0.7, C=C),
    svm.SVC(kernel="poly", degree=3, gamma="auto", C=C),
)
models = (clf.fit(X, y) for clf in models)
```
