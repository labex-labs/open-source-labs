# 重要度に基づいた特徴の選択

係数に基づいて最も重要な2つの特徴を`SelectFromModel`を使って選択します。`SelectFromModel`は`threshold`パラメータを受け付け、重要度（係数によって定義される）がこの閾値を超える特徴を選択します。

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```
