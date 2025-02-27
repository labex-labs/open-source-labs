# Erstellen der Pipeline für Self-Training

In diesem Schritt erstellen wir eine Pipeline für halbüberwachtes Lernen unter Verwendung von Self-Training. Die Pipeline wird der überwachten Pipeline ähneln, aber wir werden den SelfTrainingClassifier anstelle des SGDClassifier verwenden.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Erstellen der Self-Training-Pipeline
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
