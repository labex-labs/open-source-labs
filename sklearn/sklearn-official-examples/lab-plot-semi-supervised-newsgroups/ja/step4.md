# Self-Training のパイプラインの作成

このステップでは、Self-Training を用いた半教師あり学習のパイプラインを作成します。このパイプラインは教師あり学習のパイプラインと似ていますが、SGDClassifier の代わりに SelfTrainingClassifier を使用します。

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Self-Training のパイプラインを作成する
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
