# 추정기 학습 및 평가

다음 단계는 각 중단 기준을 사용하여 추정기를 학습하고 평가하는 것입니다. 루프를 사용하여 각 추정기와 중단 기준을 반복하고, 다른 최대 반복 횟수를 반복하는 또 다른 루프를 사용할 것입니다. 그런 다음 결과를 pandas 데이터프레임에 저장하여 플롯하기 쉽게 만들 것입니다.

```python
results = []
for estimator_name, estimator in estimator_dict.items():
    print(estimator_name + ": ", end="")
    for max_iter in range(1, 50):
        print(".", end="")
        sys.stdout.flush()

        fit_time, n_iter, train_score, test_score = fit_and_score(
            estimator, max_iter, X_train, X_test, y_train, y_test
        )

        results.append(
            (estimator_name, max_iter, fit_time, n_iter, train_score, test_score)
        )
    print("")

# 결과를 pandas 데이터프레임으로 변환하여 플롯하기 쉽게 만듭니다.
columns = [
    "중단 기준",
    "max_iter",
    "학습 시간 (초)",
    "n_iter_",
    "훈련 점수",
    "테스트 점수",
]
results_df = pd.DataFrame(results, columns=columns)
```
