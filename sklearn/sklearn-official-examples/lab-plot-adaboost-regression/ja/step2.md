# 決定木とAdaBoost回帰器を使った学習と予測

ここでは、分類器を定義してデータに適合させます。最初の回帰器を`max_depth=4`の`DecisionTreeRegressor`として定義します。2番目の回帰器を、`max_depth=4`の`DecisionTreeRegressor`をベース学習器とする`AdaBoostRegressor`として定義します。それらのベース学習器を`n_estimators=300`で持つAdaBoost回帰器を構築します。その後、両方の回帰器をデータに適合させ、同じデータに対して予測を行って、それらがどの程度データに適合するかを見ます。

```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
)

regr_1.fit(X, y)
regr_2.fit(X, y)

y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)
```
