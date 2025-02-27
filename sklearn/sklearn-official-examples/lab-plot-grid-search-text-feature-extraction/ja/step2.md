# ハイパーパラメータチューニングを伴うパイプラインの定義

テキスト分類のために、テキストの特徴ベクトル化器と単純な分類器を組み合わせたパイプラインを定義します。分類器として Complement Naive Bayes を、特徴抽出には TfidfVectorizer を使用します。

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
    "vect__ngram_range": ((1, 1), (1, 2)),  # unigrams or bigrams
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}

```
