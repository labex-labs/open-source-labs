# LDA 적용

tf 특징을 사용하여 LDA 모델을 적용합니다.

```python
from sklearn.decomposition import LatentDirichletAllocation

print(
    "\n" * 2,
    "tf 특징, n_samples=%d 및 n_features=%d를 사용하여 LDA 모델을 맞추는 중..."
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
print("done in %0.3fs." % (time() - t0))

tf_feature_names = tf_vectorizer.get_feature_names_out()
plot_top_words(lda, tf_feature_names, n_top_words, "LDA 모델의 주제")
```
