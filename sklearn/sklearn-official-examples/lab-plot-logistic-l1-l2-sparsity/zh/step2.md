# 加载数据集

我们将使用`datasets.load_digits(return_X_y=True)`加载数字数据集。我们还将使用`StandardScaler().fit_transform(X)`对数据进行标准化。目标变量将是二元的，其中0 - 4将被分类为0，5 - 9将被分类为1。

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
