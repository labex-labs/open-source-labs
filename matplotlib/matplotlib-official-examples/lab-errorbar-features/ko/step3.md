# 오차 값 정의

이제 오차 값을 정의합니다. 이 예제에서는 `error` 변수를 사용하여 대칭 오차를 나타내고, `asymmetric_error` 변수를 사용하여 비대칭 오차를 나타냅니다.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
