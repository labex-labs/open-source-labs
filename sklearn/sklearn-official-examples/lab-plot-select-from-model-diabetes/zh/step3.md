# 根据重要性选择特征

我们使用 `SelectFromModel` 根据系数选择最重要的两个特征。`SelectFromModel` 接受一个 `threshold` 参数，并将选择重要性（由系数定义）高于此阈值的特征。

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```
