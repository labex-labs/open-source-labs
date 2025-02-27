# 再帰的特徴削除

再帰的特徴削除 (RFE) は、最も重要な特徴を選択するために、徐々に小さくなる特徴のセットを再帰的に考慮する特徴選択方法です。これは、特徴に割り当てられた重み付きで外部推定器を訓練し、最も重要でない特徴を削除することによって機能します。

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Iris データセットを読み込む
X, y = load_iris(return_X_y=True)

# 外部推定器として SVC を初期化する
estimator = SVC(kernel="linear")

# 外部推定器と 2 つの特徴を選択するように RFE を初期化する
selector = RFE(estimator, n_features_to_select=2)

# 最適な特徴を選択する
X_selected = selector.fit_transform(X, y)

print("元の X の形状:", X.shape)
print("選択された特徴を持つ X の形状:", X_selected.shape)
print("選択された特徴:", selector.get_support(indices=True))
```

この例では、外部推定器としてサポートベクトル分類器 (SVC) を使って、Iris データセットから 2 つの最適な特徴を選択します。出力には、データセットの元の形状と、最適な特徴を選択した後の形状が表示されます。
