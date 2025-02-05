# 根据系数确定特征重要性

为了了解特征的重要性，我们使用岭回归交叉验证（RidgeCV）估计器。具有最高绝对 `coef_` 值的特征被认为是最重要的。

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```
