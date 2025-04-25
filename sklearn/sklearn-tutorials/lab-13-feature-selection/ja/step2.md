# 単変量特徴選択

単変量特徴選択は、単変量統計検定に基づいて最適な特徴を選択することによって機能します。scikit-learn には、単変量特徴選択を実装するいくつかのクラスがあります。

- `SelectKBest`：上位 k 個の最も高いスコアを持つ特徴を選択します
- `SelectPercentile`：ユーザ指定の割合の最も高いスコアを持つ特徴を選択します
- `SelectFpr`：偽陽性率に基づいて特徴を選択します
- `SelectFdr`：偽発見率に基づいて特徴を選択します
- `SelectFwe`：家族全体の誤差に基づいて特徴を選択します
- `GenericUnivariateSelect`：構成可能な戦略を使った選択を可能にします

ここでは、Iris データセットから 2 つの最適な特徴を選択するために `SelectKBest` を使う例を示します。

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Iris データセットを読み込む
X, y = load_iris(return_X_y=True)

# f_classif スコア関数と k=2 で SelectKBest を初期化する
selector = SelectKBest(f_classif, k=2)

# 最適な特徴を選択する
X_selected = selector.fit_transform(X, y)

print("元の X の形状：", X.shape)
print("選択された特徴を持つ X の形状：", X_selected.shape)
print("選択された特徴：", selector.get_support(indices=True))
```

この例では、`f_classif` スコア関数を使って、Iris データセットから 2 つの最適な特徴を選択します。出力には、データセットの元の形状と、最適な特徴を選択した後の形状が表示されます。
