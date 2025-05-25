# 하이퍼파라미터 최적화를 위한 랜덤 검색

랜덤 검색을 사용하여 하이퍼파라미터 공간을 탐색하고 SVM 모델에 대한 최적의 하이퍼파라미터를 찾습니다.

```python
# 샘플링할 파라미터 및 분포 지정
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# 랜덤 검색 실행
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV 가 %d개의 후보 파라미터 설정에 %.2f 초가 소요되었습니다."
    % ((time() - start), n_iter_search)
)

# 결과 출력
report(random_search.cv_results_)
```
