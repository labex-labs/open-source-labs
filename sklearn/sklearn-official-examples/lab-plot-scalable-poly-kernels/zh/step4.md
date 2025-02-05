# 建立核支持向量机模型

我们将训练一个核支持向量机（SVM），以了解PolynomialCountSketch在近似核性能方面的表现如何。

```python
from sklearn.svm import SVC

# 训练一个核支持向量机
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# 打印核支持向量机的准确率
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
