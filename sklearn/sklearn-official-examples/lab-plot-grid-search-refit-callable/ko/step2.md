# 함수 정의

이 실습에서 나중에 사용될 두 가지 함수를 정의합니다.

```python
def lower_bound(cv_results):
    """
    최고 `mean_test_scores`의 1 표준 편차 내의 하한을 계산합니다.

    매개변수
    ----------
    cv_results : numpy(masked) ndarrays의 사전
        `GridSearchCV`의 속성 cv_results_ 참조

    반환값
    -------
    float
        최고 `mean_test_score`의 1 표준 편차 내의 하한.
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    모델 복잡성과 교차 검증 점수를 균형 있게 조정합니다.

    매개변수
    ----------
    cv_results : numpy(masked) ndarrays의 사전
        `GridSearchCV`의 속성 cv_results_ 참조

    반환값
    ------
    int
        최고 `mean_test_score`의 1 표준 편차 내에 있는 점수를 가지면서
        PCA 성분이 가장 적은 모델의 인덱스.
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
