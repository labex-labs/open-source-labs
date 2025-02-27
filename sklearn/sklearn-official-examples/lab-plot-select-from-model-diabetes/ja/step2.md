# 係数からの特徴の重要度

特徴の重要度を把握するために、RidgeCV推定器を使用します。絶対値が最も高い`coef_`値を持つ特徴が最も重要であると考えられます。

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```
