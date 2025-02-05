# 准备数据

在这一步中，我们将为特征离散化准备合成分类数据集。我们将使用scikit-learn库生成三个不同的数据集：月牙形、同心圆和线性可分数据。

```python
h = 0.02  # 网格中的步长

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
