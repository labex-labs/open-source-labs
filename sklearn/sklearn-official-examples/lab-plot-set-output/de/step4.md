# Konfiguriere einen Pipeline, um DataFrames auszugeben

In einer `pipeline.Pipeline` konfiguriert `set_output` alle Schritte, um DataFrames auszugeben.

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
