# 하이퍼파라미터 튜닝

랜덤 검색 (RandomizedSearchCV) 을 사용하여 하이퍼파라미터 그리드를 탐색하고 파이프라인에 대한 최상의 하이퍼파라미터 조합을 찾습니다. 이 경우 `n_iter=40`으로 검색 공간을 제한합니다. 더욱 정보적인 분석을 위해 `n_iter` 값을 늘릴 수 있지만, 계산 시간이 증가합니다.

```python
from pprint import pprint
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)
```
