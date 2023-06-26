# Constructing a Simple Pipeline with a Preprocessing Step and Classifier

In this step, we will construct a simple pipeline with a preprocessing step and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Next, we define the steps of the pipeline:

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

Then, we create the pipeline:

```python
pipe = Pipeline(steps)
```

Finally, we display the visual representation of the pipeline:

```python
set_config(display="diagram")
pipe
```
