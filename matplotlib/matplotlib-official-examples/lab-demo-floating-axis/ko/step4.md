# 호스트 축 생성

이 단계에서는 호스트 축을 생성하고 그리드 헬퍼를 설정합니다. `fig.add_subplot()`을 사용하여 호스트 축을 생성합니다.

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
