# 개별 타원 그리기

이 예제에서는 임의의 크기, 위치 및 색상을 가진 여러 타원을 그립니다. 각 타원은 `Ellipse` 클래스의 인스턴스가 됩니다.

```python
# 재현성을 위해 난수 상태 고정
np.random.seed(19680801)

# 그릴 타원의 수
NUM = 250

# 타원 생성
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# 플롯을 생성하고 종횡비를 'equal'로 설정
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# 각 타원을 플롯에 추가
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# 플롯의 x 및 y 제한 설정
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# 플롯 표시
plt.show()
```
