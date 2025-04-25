# 加载数据

接下来，我们将从 scikit-learn 中加载鸢尾花数据集。这个数据集是一个经典的机器学习数据集，由鸢尾花的测量数据及其物种标签组成。

```python
iris = load_iris()
X = iris.data
y = iris.target
```
