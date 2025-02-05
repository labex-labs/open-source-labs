# 定义带有超参数调整的管道

我们定义一个管道，它将文本特征向量化器与用于文本分类的简单分类器相结合。我们将使用互补朴素贝叶斯（Complement Naive Bayes）作为分类器，并使用词频 - 逆文档频率向量化器（TfidfVectorizer）进行特征提取。

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline
import numpy as np

pipeline = Pipeline(
    [
        ("vect", TfidfVectorizer()),
        ("clf", ComplementNB()),
    ]
)

parameter_grid = {
    "vect__max_df": (0.2, 0.4, 0.6, 0.8, 1.0),
    "vect__min_df": (1, 3, 5, 10),
    "vect__ngram_range": ((1, 1), (1, 2)),  # 一元语法或二元语法
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}

```
