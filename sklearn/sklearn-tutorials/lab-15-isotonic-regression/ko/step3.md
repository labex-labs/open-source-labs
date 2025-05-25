# 등장값 회귀 모델 적합

이제 우리의 데이터에 등장값 회귀 모델을 적합할 수 있습니다. `IsotonicRegression` 클래스의 인스턴스를 생성하고 입력 데이터와 대상 값을 사용하여 `fit` 메서드를 호출합니다.

```python
# 등장값 회귀 모델 적합
ir = IsotonicRegression()
ir.fit(X, y)
```
