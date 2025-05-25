# 파이프라인을 DataFrame 출력으로 설정

`pipeline.Pipeline`에서 `set_output`를 사용하면 모든 단계가 DataFrame 을 출력하도록 설정됩니다.

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
