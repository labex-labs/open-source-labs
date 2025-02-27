# SelectFromModel を使った特徴選択

`SelectFromModel` クラスは、各特徴に重要度を割り当てる任意の推定器とともに使用できるメタ変換器です。これは、特徴の重要度に基づいて特徴を選択し、指定された閾値未満の特徴を削除します。

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Iris データセットを読み込む
X, y = load_iris(return_X_y=True)

# 推定器として RandomForestClassifier を初期化する
estimator = RandomForestClassifier()

# 推定器と "mean" の閾値で SelectFromModel を初期化する
selector = SelectFromModel(estimator, threshold="mean")

# 最適な特徴を選択する
X_selected = selector.fit_transform(X, y)

print("元の X の形状:", X.shape)
print("選択された特徴を持つ X の形状:", X_selected.shape)
print("選択された特徴:", selector.get_support(indices=True))
```

この例では、推定器としてランダムフォレスト分類器を使用し、平均重要度よりも高い重要度を持つ特徴を選択します。出力には、データセットの元の形状と、最適な特徴を選択した後の形状が表示されます。
