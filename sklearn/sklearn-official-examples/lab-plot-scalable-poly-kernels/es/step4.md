# Establecer el Modelo de SVM Kernelizado

Entrenaremos un SVM kernelizado para ver qué tan bien PolynomialCountSketch está aproximando el rendimiento del kernel.

```python
from sklearn.svm import SVC

# Entrenar un SVM kernelizado
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# Mostrar la precisión del SVM kernelizado
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
