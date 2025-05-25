# 이상치 예측 함수

다음 단계는 이상치 예측 함수를 정의하는 것입니다. 이 예제에서는 `LocalOutlierFactor` 및 `IsolationForest` 알고리즘을 사용합니다. `compute_prediction` 함수는 X 의 평균 이상치 점수를 반환합니다.

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Computing {model_name} prediction...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
