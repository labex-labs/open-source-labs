# 导入库并加载数据集

让我们首先导入必要的库并加载鸢尾花数据集。我们将使用 `sklearn.datasets` 模块中的 `load_iris` 函数来加载数据集。

```python
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 目标变量

print("样本数量:", X.shape[0])
print("特征数量:", X.shape[1])
print("类别数量:", len(set(y)))
```
