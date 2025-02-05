# 递归特征消除

递归特征消除（RFE）是一种特征选择方法，它通过递归地考虑越来越小的特征集来选择最重要的特征。其工作原理是使用分配给特征的权重训练一个外部估计器，并修剪最不重要的特征。

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# 加载鸢尾花数据集
X, y = load_iris(return_X_y=True)

# 将支持向量分类器（SVC）初始化为外部估计器
estimator = SVC(kernel="linear")

# 使用外部估计器初始化RFE并选择2个特征
selector = RFE(estimator, n_features_to_select=2)

# 选择最佳特征
X_selected = selector.fit_transform(X, y)

print("原始X的形状:", X.shape)
print("选择特征后的X形状:", X_selected.shape)
print("选择的特征:", selector.get_support(indices=True))
```

在这个示例中，我们使用支持向量分类器（SVC）作为外部估计器，并从鸢尾花数据集中选择两个最佳特征。输出将显示数据集的原始形状以及选择最佳特征后的形状。
