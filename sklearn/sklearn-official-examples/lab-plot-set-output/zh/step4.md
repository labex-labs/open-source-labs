# 配置管道以输出 DataFrame

在`pipeline.Pipeline`中，`set_output`会将所有步骤配置为输出 DataFrame。

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
