# 定义管道组件

我们将定义管道组件，包括主成分分析（PCA）、标准化缩放器（Standard Scaler）和逻辑回归。为了使示例运行得更快，我们将容差设置为一个较大的值。

```python
# 定义一个管道，用于搜索主成分分析（PCA）截断和分类器正则化的最佳组合。
pca = PCA()
# 定义一个标准化缩放器，用于标准化输入
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
