# F-검정 계산

이제 각 특징에 대한 F-검정 점수를 계산합니다. F-검정은 변수 간의 선형 종속성만 포착합니다. F-검정 점수를 최대 F-검정 점수로 나누어 정규화할 것입니다.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```
