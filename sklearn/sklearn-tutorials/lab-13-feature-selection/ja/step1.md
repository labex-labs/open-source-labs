# 分散の低い特徴の削除

scikit-learn の `VarianceThreshold` クラスを使って、分散の低い特徴を削除することができます。分散の低い特徴は、通常、モデルにとってあまり情報を提供しません。ここでは、`VarianceThreshold` を使ってゼロ分散の特徴を削除する方法を示します。

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# 分散の 80% の閾値で VarianceThreshold を初期化
sel = VarianceThreshold(threshold=(.8 * (1 -.8)))

# 高い分散を持つ特徴を選択
X_selected = sel.fit_transform(X)

print("元の X の形状：", X.shape)
print("選択された特徴を持つ X の形状：", X_selected.shape)
print("選択された特徴：", sel.get_support(indices=True))
```

このコード スニペットは、データセットからゼロ分散の特徴を削除するために `VarianceThreshold` をどのように使うかを示しています。出力には、データセットの元の形状と、高い分散を持つ特徴を選択した後の形状が表示されます。
