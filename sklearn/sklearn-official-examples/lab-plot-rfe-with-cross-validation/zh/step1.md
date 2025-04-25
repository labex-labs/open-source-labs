# 数据生成

我们将使用 scikit-learn 的`make_classification`函数生成一个分类任务。我们将生成 500 个样本，每个样本有 15 个特征，其中 3 个是信息性的，2 个是冗余的，10 个是非信息性的。

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```
