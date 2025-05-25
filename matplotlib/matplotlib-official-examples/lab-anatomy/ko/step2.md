# 그림 생성 및 축 설정

다음으로, 그림을 생성하고 축을 설정합니다. `add_axes()` 메서드를 사용하여 그림 내에 새로운 축 집합을 생성합니다. 또한 x 및 y 축의 제한을 설정하고 그리드 선을 추가합니다.

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
