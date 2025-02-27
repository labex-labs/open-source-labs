# Erstelle die Pipeline für LabelSpreading

In diesem Schritt werden wir eine Pipeline für das halbüberwachte Lernen mit LabelSpreading erstellen. Die Pipeline wird der überwachten Pipeline ähneln, aber wir werden das LabelSpreading-Algorithmus statt des SGDClassifier verwenden.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Erstelle die LabelSpreading-Pipeline
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```