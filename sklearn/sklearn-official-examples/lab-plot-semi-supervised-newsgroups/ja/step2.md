# 教師あり学習のパイプラインの作成

このステップでは、教師あり学習のパイプラインを作成します。このパイプラインは、テキストデータをトークンの出現回数の行列に変換する CountVectorizer、出現回数行列に対して単語頻度 - 逆文書頻度（TF-IDF）正規化を適用する TfidfTransformer、およびモデルを学習させる SGDClassifier で構成されます。

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# SGDClassifier のパラメータ
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# CountVectorizer のパラメータ
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# パイプラインを作成する
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```
