# T 分布確率近傍埋め込み

これは、データポイント間の類似性を結合確率に変換し、低次元埋め込みと高次元データの結合確率間のクルバック・ライブラー収束を最小化しようとします。

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```
