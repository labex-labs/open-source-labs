# Constructing a Pipeline Chaining Multiple Preprocessing Steps & Classifier

In this step, we will construct a pipeline with multiple preprocessing steps and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Next, we define the steps of the pipeline:

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

Then, we create the pipeline:

```python
pipe = Pipeline(steps)
```

Finally, we display the visual representation of the pipeline:

```python
pipe
```


