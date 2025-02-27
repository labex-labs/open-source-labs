# 線形回帰モデルをフィットさせる

次に、学習用セットに線形回帰モデルをフィットさせます。

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
