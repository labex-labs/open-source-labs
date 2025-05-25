# 그리드 검색 전략 정의

`GridSearchCV` 인스턴스의 `refit` 매개변수에 전달될 함수를 정의합니다. 이 함수는 `GridSearchCV`의 `cv_results_` 속성에서 최상의 후보를 선택하는 사용자 정의 전략을 구현합니다. 후보가 선택되면 `GridSearchCV` 인스턴스가 자동으로 재학습합니다.

여기서 전략은 정밀도와 재현율 측면에서 최상의 모델을 짧은 목록으로 만드는 것입니다. 선택된 모델 중에서 예측 속도가 가장 빠른 모델을 최종적으로 선택합니다. 이러한 사용자 정의 선택은 완전히 임의적임을 유의하십시오.

```python
import pandas as pd
from sklearn.metrics import classification_report

def print_dataframe(filtered_cv_results):
    """필터링된 데이터프레임을 보기 좋게 출력합니다."""
    for mean_precision, std_precision, mean_recall, std_recall, params in zip(
        filtered_cv_results["mean_test_precision"],
        filtered_cv_results["std_test_precision"],
        filtered_cv_results["mean_test_recall"],
        filtered_cv_results["std_test_recall"],
        filtered_cv_results["params"],
    ):
        print(
            f"정밀도: {mean_precision:0.3f} (±{std_precision:0.03f}),"
            f" 재현율: {mean_recall:0.3f} (±{std_recall:0.03f}),"
            f" 파라미터: {params}"
        )
    print()


def refit_strategy(cv_results):
    """최상의 추정자를 선택하는 전략을 정의합니다.

    여기서 정의된 전략은 정밀도 임계값 0.98 미만의 모든 결과를 필터링하고, 나머지를 재현율 기준으로 순위를 매기고, 최상의 재현율 모델의 표준 편차 내에 있는 모든 모델을 유지하는 것입니다. 이러한 모델이 선택되면 예측 속도가 가장 빠른 모델을 선택할 수 있습니다.

    매개변수
    ----------
    cv_results : numpy (마스크) ndarrays 의 사전
        `GridSearchCV` 에 의해 반환된 CV 결과.

    반환값
    -------
    best_index : int
        `cv_results` 에 나타나는 최상의 추정자의 인덱스.
    """
    # 다양한 점수에 대한 그리드 검색 정보를 출력합니다.
    precision_threshold = 0.98

    cv_results_ = pd.DataFrame(cv_results)
    print("모든 그리드 검색 결과:")
    print_dataframe(cv_results_)

    # 임계값 미만의 모든 결과를 필터링합니다.
    high_precision_cv_results = cv_results_[
        cv_results_["mean_test_precision"] > precision_threshold
    ]

    print(f"정밀도가 {precision_threshold}보다 높은 모델:")
    print_dataframe(high_precision_cv_results)

    # 재현율 측면에서 가장 성능이 좋은 모델을 선택합니다.
    # (최상의 모델로부터 1 시그마 내에 있는 모델)
    best_recall_std = high_precision_cv_results["mean_test_recall"].std()
    best_recall = high_precision_cv_results["mean_test_recall"].max()
    best_recall_threshold = best_recall - best_recall_std

    high_recall_cv_results = high_precision_cv_results[
        high_precision_cv_results["mean_test_recall"] > best_recall_threshold
    ]
    print(
        "이전에 선택된 높은 정밀도 모델 중에서,\n"
        "최고 재현율 모델의 표준 편차 내에 있는 모든 모델을 유지합니다:"
    )
    print_dataframe(high_recall_cv_results)

    # 최상의 후보 중에서 예측 속도가 가장 빠른 모델을 선택합니다.
    fastest_top_recall_high_precision_index = high_recall_cv_results[
        "mean_score_time"
    ].idxmin()

    print(
        "\n선택된 최종 모델은 정밀도와 재현율 기준으로 이전에 선택된 최상의 모델 집합 중 예측 속도가 가장 빠른 모델입니다.\n"
        "그 실행 시간은 다음과 같습니다:\n\n"
        f"{high_recall_cv_results.loc[fastest_top_recall_high_precision_index]}"
    )

    return fastest_top_recall_high_precision_index
```
