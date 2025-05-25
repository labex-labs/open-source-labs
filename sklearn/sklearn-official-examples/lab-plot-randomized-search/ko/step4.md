# 그리드 검색을 통한 하이퍼파라미터 최적화

그리드 검색을 사용하여 하이퍼파라미터 공간을 탐색하고 SVM 모델에 대한 최적의 하이퍼파라미터를 찾습니다.

```python
# 검색할 파라미터 지정
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# 그리드 검색 실행
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV 가 %d개의 후보 파라미터 설정에 %.2f 초가 소요되었습니다."
    % (len(grid_search.cv_results_["params"]), time() - start)
)

# 결과 출력
report(grid_search.cv_results_)
```
