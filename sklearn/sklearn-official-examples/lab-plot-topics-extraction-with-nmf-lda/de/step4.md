# Wendet LDA an

Wir werden LDA-Modelle mit tf-Merkmalen anwenden.

```python
from sklearn.decomposition import LatentDirichletAllocation

print(
    "\n" * 2,
    "Passt LDA-Modelle mit tf-Merkmalen an, n_samples=%d und n_features=%d..."
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
print("fertig in %0.3fs." % (time() - t0))

tf_feature_names = tf_vectorizer.get_feature_names_out()
plot_top_words(lda, tf_feature_names, n_top_words, "Topics in LDA model")
```
