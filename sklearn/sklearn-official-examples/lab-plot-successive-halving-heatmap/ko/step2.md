# 격자 검색 수행

SVC 모델에 대한 매개변수 검색을 위해 격자 검색을 사용할 것입니다. 1 단계에서 생성된 합성 데이터셋과 매개변수 그리드를 사용할 것입니다.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
