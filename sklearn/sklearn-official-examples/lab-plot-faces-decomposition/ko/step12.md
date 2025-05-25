# 사전 학습 - 양의 사전 및 코드

```python
dict_pos_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components,
    alpha=0.1,
    max_iter=50,
    batch_size=3,
    fit_algorithm="cd",
    random_state=rng,
    positive_dict=True,
    positive_code=True,
)
dict_pos_estimator.fit(faces_centered)
plot_gallery(
    "사전 학습 - 양의 사전 및 코드",
    dict_pos_estimator.components_[:n_components],
    cmap=plt.cm.RdBu,
)
```
