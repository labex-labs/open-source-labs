# 加载鸢尾花数据集

我们将使用Scikit-learn内置的`load_iris`函数来加载鸢尾花数据集。

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # 我们只取前两个特征。
y = iris.target
```
