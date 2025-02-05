# 加载数据集并为GridSearchCV定义参数

我们将加载数字数据集，并为GridSearchCV定义参数。我们将设置主成分分析（PCA）截断和分类器正则化的参数。

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
