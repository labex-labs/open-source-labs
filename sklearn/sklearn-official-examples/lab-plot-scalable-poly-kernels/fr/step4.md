# Établir le modèle SVM à noyau

Nous allons entraîner un SVM à noyau pour voir à quel point PolynomialCountSketch approche les performances du noyau.

```python
from sklearn.svm import SVC

# Entraîner un SVM à noyau
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# Afficher la précision du SVM à noyau
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
