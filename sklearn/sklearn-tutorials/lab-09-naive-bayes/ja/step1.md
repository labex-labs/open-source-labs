# ライブラリのインポートとデータセットの読み込み

必要なライブラリをインポートしてアイリスデータセットを読み込みましょう。データセットを読み込むために、`sklearn.datasets`モジュールの`load_iris`関数を使います。

```python
from sklearn.datasets import load_iris

# アイリスデータセットを読み込む
iris = load_iris()
X = iris.data  # 特徴量
y = iris.target  # 目的変数

print("サンプル数：", X.shape[0])
print("特徴量数：", X.shape[1])
print("クラス数：", len(set(y)))
```
