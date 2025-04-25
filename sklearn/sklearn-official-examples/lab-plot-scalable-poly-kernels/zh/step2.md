# 建立基线模型

我们将在原始特征上训练一个线性支持向量机（SVM）来建立一个基线模型，并打印其准确率。

```python
from sklearn.svm import LinearSVC

# 在原始特征上训练一个线性 SVM
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# 打印基线模型的准确率
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
