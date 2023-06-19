# Create the Pipeline for LabelSpreading

In this step, we will create a pipeline for semi-supervised learning using LabelSpreading. The pipeline will be similar to the supervised pipeline, but we will use the LabelSpreading algorithm instead of the SGDClassifier.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Create the LabelSpreading pipeline
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```


