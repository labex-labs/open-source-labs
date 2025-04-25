# 使用 SelectFromModel 进行特征选择

`SelectFromModel`类是一个元变换器，可与任何为每个特征分配重要性的估计器一起使用。它根据特征的重要性进行选择，并移除低于指定阈值的特征。

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# 加载鸢尾花数据集
X, y = load_iris(return_X_y=True)

# 将随机森林分类器（RandomForestClassifier）初始化为估计器
estimator = RandomForestClassifier()

# 使用估计器和“均值”阈值初始化 SelectFromModel
selector = SelectFromModel(estimator, threshold="mean")

# 选择最佳特征
X_selected = selector.fit_transform(X, y)

print("原始 X 的形状：", X.shape)
print("选择特征后的 X 形状：", X_selected.shape)
print("选择的特征：", selector.get_support(indices=True))
```

在这个示例中，我们使用随机森林分类器作为估计器，并选择重要性大于平均重要性的特征。输出将显示数据集的原始形状以及选择最佳特征后的形状。
