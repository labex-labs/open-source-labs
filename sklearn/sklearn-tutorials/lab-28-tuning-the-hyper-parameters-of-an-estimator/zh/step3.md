# 定义估计器和参数网格

现在我们需要定义想要调整的估计器以及要搜索的参数网格。参数网格指定了我们想要为每个超参数尝试的值。

```python
from sklearn.svm import SVC

# 创建支持向量分类器的实例
svc = SVC()

# 定义参数网格
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
