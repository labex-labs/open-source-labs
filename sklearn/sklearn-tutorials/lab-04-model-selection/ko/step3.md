# 그리드 검색

그리드 검색은 추정자에 대한 최상의 매개변수 값 조합을 찾는 데 사용할 수 있는 기술입니다. 매개변수 값의 그리드를 지정하고, 각 매개변수 조합에 대해 학습 데이터에 추정자를 맞추고, 가장 높은 교차 검증 점수를 생성하는 매개변수를 선택하는 것을 포함합니다.

```python
from sklearn.model_selection import GridSearchCV

# 매개변수 값의 그리드 정의
Cs = np.logspace(-6, -1, 10)

# SVM 분류기와 매개변수 그리드를 사용하여 GridSearchCV 객체 생성
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# 학습 데이터에 GridSearchCV 객체 맞추기
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
