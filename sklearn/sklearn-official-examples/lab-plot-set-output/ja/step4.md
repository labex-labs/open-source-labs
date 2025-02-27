# パイプラインを設定して DataFrame を出力する

`pipeline.Pipeline` では、`set_output` を使用してすべてのステップを設定して DataFrame を出力します。

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
