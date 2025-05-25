# 연속 반복 검색 수행

이제 2 단계에서 사용된 동일한 SVC 모델과 데이터셋에 대해 연속 반복 검색 (Successive Halving) 을 사용하여 매개변수 검색을 수행할 것입니다.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
