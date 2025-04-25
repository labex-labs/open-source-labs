# 加载数据

我们将使用 scikit-learn 中的鸢尾花数据集。该数据集包含 150 个样本，每个样本有四个特征和一个目标标签。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
