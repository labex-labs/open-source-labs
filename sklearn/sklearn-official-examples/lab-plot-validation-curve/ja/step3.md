# 検証スコアの計算

異なる gamma 値の SVM 分類器に対する学習スコアと検証スコアを計算するために、scikit-learn の `validation_curve` 関数を使用します。

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```
