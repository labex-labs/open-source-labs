# 2値分類用のデータセットを生成する

次に、scikit - learnが提供する`make_classification`関数を使って2値分類用のデータセットを生成します。この関数を使うと、サンプル数、特徴量数、クラスごとのクラスタ数、情報的な特徴量数を指定できます。再現性を保証するために、固定された乱数シード値を使います。

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```
