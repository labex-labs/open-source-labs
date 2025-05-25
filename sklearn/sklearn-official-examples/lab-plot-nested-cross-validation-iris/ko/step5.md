# 중첩 교차 검증

모델과 그 하이퍼파라미터의 일반화 오차를 추정하기 위해 중첩 교차 검증을 사용합니다. 내부 루프에서 각 학습 집합에 대한 최상의 하이퍼파라미터를 찾기 위해 그리드 검색을 수행합니다. 외부 루프에서 테스트 집합에 대한 모델의 성능을 평가합니다.

```python
from sklearn.model_selection import KFold, cross_val_score

# 임의 시도 횟수
NUM_TRIALS = 30

# 점수 저장을 위한 배열
non_nested_scores = np.zeros(NUM_TRIALS)
nested_scores = np.zeros(NUM_TRIALS)

# 각 시도에 대한 루프
for i in range(NUM_TRIALS):
    # 데이터셋과 독립적으로 내부 및 외부 루프에 대한 교차 검증 기법을 선택합니다.
    inner_cv = KFold(n_splits=4, shuffle=True, random_state=i)
    outer_cv = KFold(n_splits=4, shuffle=True, random_state=i)

    # 매개변수 최적화를 포함한 중첩 CV
    clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=inner_cv)
    nested_score = cross_val_score(clf, X=X_iris, y=y_iris, cv=outer_cv)
    nested_scores[i] = nested_score.mean()

score_difference = non_nested_score - nested_scores.mean()
```
