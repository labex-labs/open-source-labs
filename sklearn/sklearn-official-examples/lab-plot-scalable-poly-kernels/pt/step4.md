# Estabelecer o Modelo SVM Kernel

Treinaremos uma SVM kernel para verificar quão bem o PolynomialCountSketch está aproximando o desempenho do kernel.

```python
from sklearn.svm import SVC

# Treinar uma SVM kernel
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# Imprimir a precisão da SVM kernel
print(f"Precisão da SVM Kernel nas características originais: {ksvm_score:.2f}%")
```
