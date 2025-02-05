# 设置标签传播分类器

我们将设置三个具有不同百分比标记数据的标签传播分类器：30%、50% 和 100%。标签传播是一种半监督学习算法，它根据标记数据点和未标记数据点之间的相似性，将标签从标记数据点传播到未标记数据点。

```python
from sklearn.semi_supervised import LabelSpreading

# 设置标签传播分类器
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # 将随机样本设置为未标记
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "Label Spreading 30% data")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "Label Spreading 50% data")
ls100 = (LabelSpreading().fit(X, y), y, "Label Spreading 100% data")
```
