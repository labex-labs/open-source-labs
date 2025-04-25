# 应用潜在狄利克雷分配（LDA）

我们将对具有词频（tf）特征的数据集应用潜在狄利克雷分配（LDA）模型。

```python
from sklearn.decomposition import LatentDirichletAllocation

print(
    "\n" * 2,
    "使用 tf 特征拟合 LDA 模型，n_samples = %d 且 n_features = %d..."
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
print("完成于 %0.3fs。" % (time() - t0))

tf_feature_names = tf_vectorizer.get_feature_names_out()
plot_top_words(lda, tf_feature_names, n_top_words, "LDA 模型中的主题")
```
