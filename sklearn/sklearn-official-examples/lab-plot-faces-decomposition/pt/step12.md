# Aprendizagem de Dicionário - Dicionário e Código Positivos

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
    "Aprendizagem de Dicionário - Dicionário e Código Positivos",
    dict_pos_estimator.components_[:n_components],
    cmap=plt.cm.RdBu,
)
```
