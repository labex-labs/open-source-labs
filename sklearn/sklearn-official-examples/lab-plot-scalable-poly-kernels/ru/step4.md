# Создание модели SVM с ядром

Мы обучим SVM с ядром, чтобы увидеть, насколько хорошо PolynomialCountSketch приближает производительность ядра.

```python
from sklearn.svm import SVC

# Обучаем SVM с ядром
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# Выводим точность SVM с ядром
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
