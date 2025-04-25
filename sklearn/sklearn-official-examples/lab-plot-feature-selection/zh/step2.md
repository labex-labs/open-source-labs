# 单变量特征选择

接下来，我们将使用 F 检验进行单变量特征选择以进行特征评分。我们将使用默认的选择函数来选择四个最显著的特征。

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
