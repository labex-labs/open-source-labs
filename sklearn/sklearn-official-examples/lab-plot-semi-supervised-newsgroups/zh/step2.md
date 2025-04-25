# 创建监督学习管道

在这一步中，我们将创建一个用于监督学习的管道。该管道将由一个 CountVectorizer（用于将文本数据转换为词元计数矩阵）、一个 TfidfTransformer（用于对计数矩阵应用词频 - 逆文档频率归一化）和一个 SGDClassifier（用于训练模型）组成。

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# SGDClassifier 的参数
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# CountVectorizer 的参数
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# 创建管道
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```
