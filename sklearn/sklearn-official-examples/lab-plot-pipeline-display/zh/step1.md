# 构建一个包含预处理步骤和分类器的简单管道

在这一步中，我们将构建一个包含预处理步骤和分类器的简单管道，并展示其可视化表示。

首先，我们导入必要的模块：

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

接下来，我们定义管道的步骤：

```python
steps = [
    ("预处理", StandardScaler()),
    ("分类器", LogisticRegression()),
]
```

然后，我们创建管道：

```python
pipe = Pipeline(steps)
```

最后，我们展示管道的可视化表示：

```python
set_config(display="diagram")
pipe
```
