# Halving Random Search 객체 생성

매개변수 공간을 탐색하기 위한 `HalvingRandomSearchCV` 객체를 생성합니다. 이 객체는 다음과 같은 인수를 받습니다.

- `estimator`: 최적화할 추정기
- `param_distributions`: 탐색할 매개변수 공간
- `factor`: 각 반복에서 후보 수를 줄이는 비율
- `random_state`: 검색에 사용되는 난수 생성기 상태

객체를 생성하는 코드는 다음과 같습니다.

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
