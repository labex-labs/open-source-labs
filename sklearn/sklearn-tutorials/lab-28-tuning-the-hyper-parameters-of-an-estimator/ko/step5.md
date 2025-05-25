# 교차 검증을 사용한 무작위 검색 수행

무작위 검색은 매개변수 그리드의 일부를 무작위로 샘플링하고, 교차 검증을 사용하여 각 조합의 성능을 평가합니다. 매개변수 공간이 크고 모든 조합을 검사하는 것이 불가능할 때 유용합니다.

```python
# RandomizedSearchCV 의 인스턴스 생성
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# 데이터를 맞추어 무작위 검색 수행
random_search.fit(X, y)

# 최상의 하이퍼파라미터 조합 출력
print('최상의 하이퍼파라미터:', random_search.best_params_)
```
