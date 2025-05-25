# 플로팅을 위한 데이터 생성

이 단계에서는 등고선 플롯에 플로팅할 데이터를 생성합니다. `np.meshgrid()` 함수를 사용하여 점의 그리드를 생성한 다음, 사인 및 코사인 함수를 사용하여 `z` 값을 계산합니다.

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
