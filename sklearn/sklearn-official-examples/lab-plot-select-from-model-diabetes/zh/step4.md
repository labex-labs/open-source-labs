# 使用顺序特征选择来选择特征

我们使用顺序特征选择器（SFS）来选择特征。SFS是一种贪心算法，在每次迭代中，我们根据交叉验证分数选择最佳的新特征添加到已选特征中。我们也可以采用相反的方向（反向SFS），即从所有特征开始，贪心选择要逐个移除的特征。

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```
