# Pipeline - Chaining Estimators

The `Pipeline` class in scikit-learn is used to chain multiple estimators into one. This allows you to call `fit` and `predict` once on your data to fit a whole sequence of estimators. It also allows for joint parameter selection and helps avoid data leakage in cross-validation.

To create a pipeline, you need to provide a list of `(key, value)` pairs, where the `key` is a string to identify each step and the `value` is an estimator object. Below is an example of creating a pipeline with a PCA transformer and an SVM classifier:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

You can access the steps of a pipeline using indexing or by name:

```python
pipe.steps[0]  # access by index
pipe[0]  # equivalent to above
pipe['reduce_dim']  # access by name
```

You can also use the `make_pipeline` function as a shorthand for constructing pipelines:

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
