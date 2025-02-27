# Erstellen der Pipeline für LabelSpreading

In diesem Schritt erstellen wir eine Pipeline für halbüberwachtes Lernen unter Verwendung von LabelSpreading. Die Pipeline wird der überwachten Pipeline ähneln, aber wir werden den LabelSpreading-Algorithmus anstelle des SGDClassifier verwenden.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Erstellen der LabelSpreading-Pipeline
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
