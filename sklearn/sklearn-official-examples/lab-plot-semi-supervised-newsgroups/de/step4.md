# Erstelle die Pipeline für das Self-Training

In diesem Schritt werden wir eine Pipeline für das halbüberwachte Lernen mit Self-Training erstellen. Die Pipeline wird der überwachten Pipeline ähneln, aber wir werden den SelfTrainingClassifier statt des SGDClassifier verwenden.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Erstelle die Self-Training-Pipeline
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```