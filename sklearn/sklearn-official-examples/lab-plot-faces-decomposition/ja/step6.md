# 辞書学習

辞書学習は、単純な要素の組み合わせとして入力データの疎表現を見つける方法であり、それらの要素が辞書を形成します。私たちは、大規模なデータセットにより適した、DictionaryLearningの高速バージョンであるMiniBatchDictionaryLearningを適用します。

```python
# 辞書学習
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Dictionary learning", batch_dict_estimator.components_[:n_components])
```
