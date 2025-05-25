# 하이퍼파라미터 최적화

이전 단계에서는 alpha 와 gamma 에 대한 기본 하이퍼파라미터 값을 사용했습니다. 모델 성능을 개선하기 위해 그리드 검색을 사용하여 이러한 하이퍼파라미터를 최적화할 수 있습니다.

```python
from sklearn.model_selection import GridSearchCV

# 파라미터 그리드 정의
param_grid = {'alpha': [1e-3, 1e-2, 1e-1, 1, 10],
              'gamma': [1e-3, 1e-2, 1e-1, 1, 10]}

# 그리드 검색 수행
grid_search = GridSearchCV(krr, param_grid, cv=5)
grid_search.fit(X, y)

# 최적 하이퍼파라미터 가져오기
best_alpha = grid_search.best_params_['alpha']
best_gamma = grid_search.best_params_['gamma']
best_krr = grid_search.best_estimator_

print("최적 alpha:", best_alpha)
print("최적 gamma:", best_gamma)
```
