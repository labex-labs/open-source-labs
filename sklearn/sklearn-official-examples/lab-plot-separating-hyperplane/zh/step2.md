# 拟合 SVM 模型

接下来，我们将使用线性核和正则化参数 1000 将 SVM 模型拟合到我们的数据集上。我们将使用 scikit-learn 中的`svm.SVC()`函数来创建 SVM 分类器。

```python
from sklearn import svm

# 拟合 SVM 模型
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
