# 加载数据集

接下来，我们将使用 scikit-learn 的 `load_iris()` 函数加载鸢尾花数据集。然后，我们将分离特征（X）和目标（y）变量。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
