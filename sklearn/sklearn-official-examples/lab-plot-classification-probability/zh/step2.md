# 加载数据集

接下来，我们从 Scikit-learn 中加载鸢尾花数据集。

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # 我们只取前两个特征用于可视化
y = iris.target
n_features = X.shape[1]
```
