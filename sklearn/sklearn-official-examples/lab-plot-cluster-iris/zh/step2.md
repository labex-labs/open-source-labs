# 加载数据

接下来，我们将加载鸢尾花数据集，它是机器学习中一个很受欢迎的数据集。这个数据集包含了不同种类鸢尾花特征的信息。我们将使用这个数据集来演示 K 均值聚类算法。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
