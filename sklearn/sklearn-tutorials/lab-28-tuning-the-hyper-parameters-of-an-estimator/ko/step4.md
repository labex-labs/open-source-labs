# 교차 검증을 사용한 그리드 검색 수행

그리드 검색은 지정된 매개변수 그리드 내에서 모든 가능한 하이퍼파라미터 조합을 철저히 검색합니다. 교차 검증을 사용하여 각 조합의 성능을 평가합니다.

```python
# GridSearchCV 의 인스턴스 생성
grid_search = GridSearchCV(svc, param_grid, cv=5)

# 데이터를 맞추어 그리드 검색 수행
grid_search.fit(X, y)

# 최상의 하이퍼파라미터 조합 출력
print('최상의 하이퍼파라미터:', grid_search.best_params_)
```
