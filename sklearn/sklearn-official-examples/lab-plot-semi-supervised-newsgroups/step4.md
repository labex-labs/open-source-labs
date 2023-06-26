# Create the Pipeline for Self-Training

In this step, we will create a pipeline for semi-supervised learning using Self-Training. The pipeline will be similar to the supervised pipeline, but we will use the SelfTrainingClassifier instead of the SGDClassifier.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Create the Self-Training pipeline
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
