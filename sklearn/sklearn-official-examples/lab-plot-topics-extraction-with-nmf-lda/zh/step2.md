# 提取特征

我们将从数据集中提取特征，对非负矩阵分解（NMF）使用词频 - 逆文档频率（tf - idf）特征，对潜在狄利克雷分配（LDA）使用原始词频特征。

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# 对NMF使用tf - idf特征。
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# 对LDA使用原始词频特征。
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```
