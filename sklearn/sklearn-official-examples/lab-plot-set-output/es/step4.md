# Configurar una tubería para que produzca DataFrames

En una `pipeline.Pipeline`, `set_output` configura todos los pasos para que produzcan DataFrames.

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
