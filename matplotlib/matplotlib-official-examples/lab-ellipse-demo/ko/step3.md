# 다양한 각도로 타원 그리기

이 예제에서는 다양한 각도를 가진 여러 타원을 그립니다. 루프를 사용하여 그리고자 하는 각도별로 `Ellipse` 인스턴스를 생성합니다.

```python
# 각도 단계 및 그릴 각도 범위 정의
angle_step = 45  # degrees
angles = np.arange(0, 180, angle_step)

# 플롯을 생성하고 종횡비를 'equal'로 설정
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# 각도에 대해 반복하고 각 각도에 대해 타원을 그립니다.
for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

# 플롯의 x 및 y 제한 설정
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# 플롯 표시
plt.show()
```
