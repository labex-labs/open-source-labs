# GridSearchCV 객체 생성 및 데이터 적합

이전 단계에서 정의한 파이프라인과 매개변수 그리드를 사용하여 `GridSearchCV` 객체를 생성합니다. 그런 다음 데이터를 객체에 맞춥니다.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
