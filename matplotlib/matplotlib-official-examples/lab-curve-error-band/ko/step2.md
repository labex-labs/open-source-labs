# 곡선 정의

다음으로, 오차 밴드를 그릴 곡선을 정의합니다. 이 예제에서는 매개변수화된 곡선을 사용합니다. 매개변수화된 곡선 x(t), y(t) 는 `~.Axes.plot`을 사용하여 직접 그릴 수 있습니다.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
