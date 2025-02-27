# Применение LDA

Мы применим модели LDA с tf признаками.

```python
from sklearn.decomposition import LatentDirichletAllocation

print(
    "\n" * 2,
    "Обучаем модели LDA с tf признаками, n_samples=%d и n_features=%d..."
    % (n_samples, n_features),
)
lda = LatentDirichletAllocation(
    n_components=n_components,
    max_iter=5,
    learning_method="online",
    learning_offset=50.0,
    random_state=0,
)
t0 = time()
lda.fit(tf)
print("завершено за %0.3fs." % (time() - t0))

tf_feature_names = tf_vectorizer.get_feature_names_out()
plot_top_words(lda, tf_feature_names, n_top_words, "Темы в модели LDA")
```
