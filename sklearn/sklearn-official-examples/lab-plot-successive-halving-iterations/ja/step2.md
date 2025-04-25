# データセットの読み込み

`sklearn.datasets`モジュールの`make_classification`関数を使って分類用のデータセットを生成します。このデータセットは 12 個の特徴量を持つ 400 個のサンプルで構成されています。データセットを読み込むコードは以下の通りです：

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
