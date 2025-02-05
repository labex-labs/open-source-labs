# 构建一个链接多个预处理步骤和分类器的管道

在这一步中，我们将构建一个包含多个预处理步骤和一个分类器的管道，并展示其可视化表示。

首先，我们导入必要的模块：

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

接下来，我们定义管道的步骤：

```python
steps = [
    ("标准缩放器", StandardScaler()),
    ("多项式特征", PolynomialFeatures(degree=3)),
    ("分类器", LogisticRegression(C=2.0)),
]
```

然后，我们创建管道：

```python
pipe = Pipeline(steps)
```

最后，我们展示管道的可视化表示：

```python
pipe
```
