# 연속적인 정규화 (Norm) 생성

데이터 포인트를 색상에 매핑하기 위해 연속적인 정규화 (norm) 를 생성합니다. `matplotlib.pyplot`의 `Normalize` 함수를 사용하여 `dydx` 값을 최소값과 최대값 사이로 정규화합니다. 그런 다음 `LineCollection` 함수를 사용하여 일련의 선분들을 생성하고, 각 선분의 미분값에 따라 개별적으로 색상을 지정합니다. `set_array` 함수를 사용하여 colormapping 에 사용되는 값을 설정합니다.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
