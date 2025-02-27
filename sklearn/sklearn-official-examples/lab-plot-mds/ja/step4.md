# MDSを実行する

次に、scikit-learnのMDSクラスを使ってノイズ付きのデータセットに対してMDSを実行します。データポイント間の対距離を既に計算済みなので、事前計算済みの非類似度オプションを使用します。2次元可視化のため、成分数を2に設定します。

```python
mds = manifold.MDS(
    n_components=2,
    max_iter=3000,
    eps=1e-9,
    random_state=seed,
    dissimilarity="precomputed",
    n_jobs=1,
    normalized_stress="auto",
)
pos = mds.fit(similarities).embedding_
```
