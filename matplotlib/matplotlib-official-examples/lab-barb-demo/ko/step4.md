# 풍향 막대 그래프 사용자 정의

barbs 함수의 매개변수를 변경하여 풍향 막대 그래프를 사용자 정의할 수 있습니다. 예를 들어, 벡터의 길이와 피벗 지점을 변경하고, 빈 막대에 대한 원을 채우고, 깃발과 막대의 색상을 변경할 수 있습니다.

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
