# 加载数据

在这一步中，我们将使用 scikit-learn 的 datasets 模块加载鸢尾花数据集。我们将选择数据集的前两个特征并将其赋值给变量 X。我们还将目标变量赋值给 Y。

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
