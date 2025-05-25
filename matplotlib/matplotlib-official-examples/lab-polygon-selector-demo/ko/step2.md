# 데이터 생성

이 단계에서는 시각화할 데이터를 생성합니다. 그리드에 점의 산점도를 생성합니다.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
