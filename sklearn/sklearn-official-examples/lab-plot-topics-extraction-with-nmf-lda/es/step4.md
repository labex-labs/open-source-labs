# Aplicar LDA

Aplicaremos modelos LDA con características tf.

```python
from sklearn.decomposition import LatentDirichletAllocation

print(
    "\n" * 2,
    "Ajustando modelos LDA con características tf, n_samples=%d y n_features=%d..."
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
print("hecho en %0.3fs." % (time() - t0))

tf_feature_names = tf_vectorizer.get_feature_names_out()
plot_top_words(lda, tf_feature_names, n_top_words, "Temas en el modelo LDA")
```
