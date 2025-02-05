# 拟合SVM模型

接下来，我们将使用线性核和正则化参数1000将SVM模型拟合到我们的数据集上。我们将使用scikit-learn中的`svm.SVC()`函数来创建SVM分类器。

```python
from sklearn import svm

# 拟合SVM模型
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
