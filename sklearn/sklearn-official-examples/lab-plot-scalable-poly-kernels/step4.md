# Establish the Kernelized SVM Model

We will train a kernelized SVM to see how well PolynomialCountSketch is approximating the performance of the kernel.

```python
from sklearn.svm import SVC

# Train a kernelized SVM
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# Print the accuracy of the kernelized SVM
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
