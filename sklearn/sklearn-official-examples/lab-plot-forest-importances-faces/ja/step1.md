# データの読み込みとモデルのフィッティング

まず、Olivetti Faces データセットを読み込み、最初の 5 クラスのみを含むようにデータセットを制限します。その後、データセットに対してランダムフォレストを学習し、不純度に基づく特徴量の重要度を評価します。タスクに使用するコア数を設定します。

```python
from sklearn.datasets import fetch_olivetti_faces

# フォレストモデルの並列フィッティングに使用するコア数を選択します。`-1` は利用可能なすべてのコアを使用することを意味します。
n_jobs = -1

# 顔のデータセットを読み込みます
data = fetch_olivetti_faces()
X, y = data.data, data.target

# データセットを 5 クラスに制限します。
mask = y < 5
X = X[mask]
y = y[mask]

# 特徴量の重要度を計算するためにランダムフォレスト分類器をフィッティングします。
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
