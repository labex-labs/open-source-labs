# 분류기 및 매개변수 정의

이 단계에서는 특징 이산화 과정에 사용할 분류기와 매개변수를 정의합니다. 로지스틱 회귀, 선형 서포트 벡터 머신 (SVM), 그래디언트 부스팅 분류기, 그리고 방사 기저 함수 커널을 사용하는 SVM 을 포함하는 분류기 목록을 생성합니다. 또한, GridSearchCV 알고리즘에 사용할 각 분류기의 매개변수 집합을 정의합니다.

```python
# (estimator, param_grid) 목록, 여기서 param_grid 는 GridSearchCV 에서 사용됩니다.
# 이 예제의 매개변수 공간은 실행 시간을 줄이기 위해 좁은 범위로 제한되어 있습니다.
# 실제 사용 사례에서는 알고리즘에 대한 더 넓은 검색 공간을 사용해야 합니다.
classifiers = [
    (
        make_pipeline(StandardScaler(), LogisticRegression(random_state=0)),
        {"logisticregression__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(StandardScaler(), LinearSVC(random_state=0, dual="auto")),
        {"linearsvc__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LogisticRegression(random_state=0),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "logisticregression__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LinearSVC(random_state=0, dual="auto"),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "linearsvc__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(), GradientBoostingClassifier(n_estimators=5, random_state=0)
        ),
        {"gradientboostingclassifier__learning_rate": np.logspace(-2, 0, 5)},
    ),
    (
        make_pipeline(StandardScaler(), SVC(random_state=0)),
        {"svc__C": np.logspace(-1, 1, 3)},
    ),
]

names = [get_name(e).replace("StandardScaler + ", "") for e, _ in classifiers]
```
