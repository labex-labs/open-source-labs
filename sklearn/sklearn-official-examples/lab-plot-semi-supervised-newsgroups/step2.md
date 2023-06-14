# Create the Pipeline for Supervised Learning

In this step, we will create a pipeline for supervised learning. The pipeline will consist of a CountVectorizer to convert the text data into a matrix of token counts, a TfidfTransformer to apply term frequency-inverse document frequency normalization to the count matrix, and an SGDClassifier to train the model.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Parameters for the SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Parameters for the CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Create the pipeline
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```


