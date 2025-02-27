# LabelSpreading のパイプラインの作成

このステップでは、LabelSpreading を用いた半教師あり学習のパイプラインを作成します。このパイプラインは教師あり学習のパイプラインと似ていますが、SGDClassifier の代わりに LabelSpreading アルゴリズムを使用します。

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# LabelSpreading のパイプラインを作成する
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
