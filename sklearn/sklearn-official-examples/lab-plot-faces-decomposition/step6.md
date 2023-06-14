# Dictionary learning

Dictionary learning is a method for finding a sparse representation of the input data as a combination of simple elements, which form a dictionary. We apply MiniBatchDictionaryLearning, which is a faster version of DictionaryLearning that is better suited for large datasets.

```python
# Dictionary learning
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Dictionary learning", batch_dict_estimator.components_[:n_components])
```


