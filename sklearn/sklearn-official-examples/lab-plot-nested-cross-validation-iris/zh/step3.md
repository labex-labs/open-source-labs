# 定义模型

我们使用具有径向基函数核的支持向量分类器。

```python
from sklearn.svm import SVC

# 我们将使用具有 "rbf" 核的支持向量分类器
svm = SVC(kernel="rbf")
```
