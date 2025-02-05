# 去除低方差特征

scikit-learn中的`VarianceThreshold`类可用于去除低方差特征。低方差特征通常无法为模型提供太多信息。我们将演示如何使用`VarianceThreshold`去除零方差特征。

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# 使用80%的可变性阈值初始化VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 -.8)))

# 选择具有高可变性的特征
X_selected = sel.fit_transform(X)

print("原始X的形状:", X.shape)
print("选择特征后的X形状:", X_selected.shape)
print("选择的特征:", sel.get_support(indices=True))
```

这段代码片段演示了如何使用`VarianceThreshold`从数据集中去除零方差特征。输出将显示数据集的原始形状以及选择具有高可变性特征后的形状。
