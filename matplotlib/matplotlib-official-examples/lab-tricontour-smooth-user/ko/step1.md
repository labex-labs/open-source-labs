# 분석 테스트 함수

이 단계에서는 삼각 측량에 대한 z-값을 생성하는 데 사용될 분석 테스트 함수를 정의합니다. 이 함수는 `function_z`라고 하며, 두 개의 인자 `x`와 `y`를 받습니다. 이 함수는 `x`와 `y`의 값을 기반으로 `z`를 계산하고, 정규화된 `z` 값을 반환합니다.

```python
def function_z(x, y):
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = -(2 * (np.exp((r1 / 10)**2) - 1) * 30. * np.cos(7. * theta1) +
          (np.exp((r2 / 10)**2) - 1) * 30. * np.cos(11. * theta2) +
          0.7 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```
