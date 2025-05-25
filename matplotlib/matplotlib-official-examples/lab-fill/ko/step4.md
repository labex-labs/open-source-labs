# 다각형 사용자 정의

`fill()` 함수에서 키워드 인자 (keyword arguments) 를 사용하여 다각형의 색상과 선 너비를 사용자 정의할 수 있습니다.

```python
x, y = koch_snowflake(order=2)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 3),
                                    subplot_kw={'aspect': 'equal'})
ax1.fill(x, y)
ax2.fill(x, y, facecolor='lightsalmon', edgecolor='orangered', linewidth=3)
ax3.fill(x, y, facecolor='none', edgecolor='purple', linewidth=3)

plt.show()
```
