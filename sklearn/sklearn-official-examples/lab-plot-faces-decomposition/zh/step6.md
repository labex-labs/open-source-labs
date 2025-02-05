# 字典学习

字典学习是一种将输入数据表示为简单元素组合的稀疏表示方法，这些简单元素构成一个字典。我们应用小批量字典学习（MiniBatchDictionaryLearning），它是字典学习（DictionaryLearning）的一个更快版本，更适合处理大型数据集。

```python
# 字典学习
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("字典学习", batch_dict_estimator.components_[:n_components])
```
