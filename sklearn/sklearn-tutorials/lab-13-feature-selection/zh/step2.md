# 单变量特征选择

单变量特征选择通过基于单变量统计检验选择最佳特征来工作。在 scikit-learn 中，有几个类实现了单变量特征选择：

- `SelectKBest`：选择得分最高的前 k 个特征
- `SelectPercentile`：选择用户指定百分比的得分最高的特征
- `SelectFpr`：基于误报率选择特征
- `SelectFdr`：基于错误发现率选择特征
- `SelectFwe`：基于族误差率选择特征
- `GenericUnivariateSelect`：允许使用可配置策略进行选择

以下是使用`SelectKBest`从鸢尾花数据集（Iris dataset）中选择两个最佳特征的示例：

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# 加载鸢尾花数据集
X, y = load_iris(return_X_y=True)

# 使用 f_classif 评分函数和 k=2 初始化 SelectKBest
selector = SelectKBest(f_classif, k=2)

# 选择最佳特征
X_selected = selector.fit_transform(X, y)

print("原始 X 的形状：", X.shape)
print("选择特征后的 X 形状：", X_selected.shape)
print("选择的特征：", selector.get_support(indices=True))
```

在这个示例中，我们使用`f_classif`评分函数并从鸢尾花数据集中选择两个最佳特征。输出将显示数据集的原始形状以及选择最佳特征后的形状。
