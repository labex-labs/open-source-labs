# 누락 값의 반복적 대체

다른 옵션으로는 IterativeImputer 가 있습니다. 이 방법은 순환 선형 회귀를 사용하여 누락된 값이 있는 각 특징을 다른 특징의 함수로 차례로 모델링합니다. 구현된 버전은 가우시안 (출력) 변수를 가정합니다. 특징이 명백하게 비정규 분포인 경우 성능을 개선하기 위해 정규 분포에 가깝도록 변환하는 것을 고려하십시오.

```python
def get_impute_iterative(X_missing, y_missing):
    imputer = IterativeImputer(
        missing_values=np.nan,
        add_indicator=True,
        random_state=0,
        n_nearest_features=3,
        max_iter=1,
        sample_posterior=True,
    )
    iterative_impute_scores = get_scores_for_imputer(imputer, X_missing, y_missing)
    return iterative_impute_scores.mean(), iterative_impute_scores.std()

mses_california[4], stds_california[4] = get_impute_iterative(
    X_miss_california, y_miss_california
)
mses_diabetes[4], stds_diabetes[4] = get_impute_iterative(
    X_miss_diabetes, y_miss_diabetes
)
x_labels.append("Iterative Imputation")

mses_diabetes = mses_diabetes * -1
mses_california = mses_california * -1
```
