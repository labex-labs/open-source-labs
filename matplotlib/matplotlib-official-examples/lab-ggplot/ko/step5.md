# 원 생성

기본 색상 순환 (color cycle) 에서 색상을 사용하여 원을 생성합니다.

```python
# 원 생성
fig, ax = plt.subplots()
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy = np.random.normal(size=2)
    ax.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
ax.axis('equal')
ax.margins(0)
plt.show()
```
