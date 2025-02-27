# Das kernelbasierte SVM-Modell etablieren

Wir werden ein kernelbasiertes SVM trainieren, um zu sehen, wie gut PolynomialCountSketch die Leistung des Kerns approximiert.

```python
from sklearn.svm import SVC

# Trainiere ein kernelbasiertes SVM
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# Gib die Genauigkeit des kernelbasierten SVMs aus
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
