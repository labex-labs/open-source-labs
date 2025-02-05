# 加载数据

接下来，我们从 Scikit-learn 中加载鸢尾花数据集，并仅选择前两个特征用于可视化。

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
