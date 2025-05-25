# 플롯 생성

플롯을 생성하고 다각형을 추가해야 합니다.

```python
fig, ax = plt.subplots()
ax.add_patch(poly)
p = PolygonInteractor(ax, poly)

ax.set_title('점을 클릭하고 드래그하여 이동')
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
plt.show()
```
