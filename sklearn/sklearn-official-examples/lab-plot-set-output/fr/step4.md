# Configurer un pipeline pour produire des DataFrames

Dans un `pipeline.Pipeline`, `set_output` configure toutes les étapes pour produire des DataFrames.

```python
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectPercentile

clf = make_pipeline(
    StandardScaler(), SelectPercentile(percentile=75), LogisticRegression()
)
clf.set_output(transform="pandas")
clf.fit(X_train, y_train)
```
