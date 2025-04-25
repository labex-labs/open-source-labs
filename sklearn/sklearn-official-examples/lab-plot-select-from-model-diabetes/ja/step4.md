# 逐次的特徴選択による特徴の選択

逐次的特徴選択器（SFS）を使って特徴を選択します。SFS は貪欲法で、各反復で、交差検証スコアに基づいて選択された特徴に追加するための最適な新しい特徴を選びます。また、逆方向（後向き SFS）にも行うことができます。つまり、すべての特徴から始めて、貪欲に 1 つずつ削除する特徴を選びます。

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```
