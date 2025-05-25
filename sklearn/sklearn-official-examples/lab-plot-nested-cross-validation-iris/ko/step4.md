# 중첩되지 않은 교차 검증

하이퍼파라미터를 조정하고 모델의 성능을 평가하기 위해 중첩되지 않은 교차 검증을 사용합니다. `GridSearchCV` 함수는 추정기의 지정된 매개변수 값에 대한 철저한 검색을 수행합니다. 4-겹 교차 검증을 사용합니다.

```python
from sklearn.model_selection import GridSearchCV

# 중첩되지 않은 매개변수 검색 및 점수 계산
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
