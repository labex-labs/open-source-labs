# 构建一个带有降维和分类器的管道

在这一步中，我们将构建一个带有降维步骤和分类器的管道，并展示其可视化表示。

首先，我们导入必要的模块：

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

接下来，我们定义管道的步骤：

```python
steps = [("降维", PCA(n_components=4)), ("分类器", SVC(kernel="linear"))]
```

然后，我们创建管道：

```python
pipe = Pipeline(steps)
```

最后，我们展示管道的可视化表示：

```python
pipe
```
