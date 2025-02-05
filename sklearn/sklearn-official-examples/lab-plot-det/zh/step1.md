# 生成合成数据

我们将使用scikit-learn的`make_classification`函数来生成合成数据。此函数会生成一个随机的n分类问题，具有n_informative个信息特征、n_redundant个冗余特征以及每个类别n_clusters_per_class个聚类。我们将生成1000个样本，有2个信息特征，随机状态设为1。然后，我们会以60/40的比例将数据拆分为训练集和测试集。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
