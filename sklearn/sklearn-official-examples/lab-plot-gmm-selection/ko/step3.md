# 모델 학습 및 선택

1 에서 6 까지의 구성 요소 수와 사용할 공분산 매개변수 유형을 변경합니다.

- `"full"`: 각 구성 요소는 고유한 일반 공분산 행렬을 가집니다.
- `"tied"`: 모든 구성 요소는 동일한 일반 공분산 행렬을 공유합니다.
- `"diag"`: 각 구성 요소는 고유한 대각 공분산 행렬을 가집니다.
- `"spherical"`: 각 구성 요소는 고유한 단일 분산을 가집니다.

다양한 모델을 평가하고 가장 좋은 모델 (가장 낮은 BIC) 을 유지합니다. 이는 `GridSearchCV`와 사용자 정의 점수 함수를 사용하여 수행됩니다. 이 함수는 음수 BIC 점수를 반환합니다. 최적의 매개변수 집합과 추정기는 각각 `best_parameters_`와 `best_estimator_`에 저장됩니다.

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """BIC 점수를 사용할 GridSearchCV 에 전달할 호출 가능 함수입니다."""
    # GridSearchCV 는 최대화할 점수를 예상하므로 음수로 만듭니다.
    return -estimator.bic(X)

param_grid = {
    "n_components": range(1, 7),
    "covariance_type": ["spherical", "tied", "diag", "full"],
}
grid_search = GridSearchCV(
    GaussianMixture(), param_grid=param_grid, scoring=gmm_bic_score
)
grid_search.fit(X)
```
