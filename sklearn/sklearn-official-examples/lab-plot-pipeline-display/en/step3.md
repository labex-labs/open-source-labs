# Constructing a Pipeline with Dimensionality Reduction and Classifier

In this step, we will construct a pipeline with a dimensionality reduction step and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Next, we define the steps of the pipeline:

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

Then, we create the pipeline:

```python
pipe = Pipeline(steps)
```

Finally, we display the visual representation of the pipeline:

```python
pipe
```
