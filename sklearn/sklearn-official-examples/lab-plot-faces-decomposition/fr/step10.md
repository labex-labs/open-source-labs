# Apprentissage de dictionnaire - dictionnaire positif

```python
dict_pos_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components,
    alpha=0.1,
    max_iter=50,
    batch_size=3,
    random_state=rng,
    positive_dict=True,
)
dict_pos_dict_estimator.fit(faces_centered)
plot_gallery(
    "Apprentissage de dictionnaire - dictionnaire positif",
    dict_pos_dict_estimator.components_[:n_components],
    cmap=plt.cm.RdBu,
)
```
