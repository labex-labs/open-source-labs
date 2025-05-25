# 색상 설정 및 PatchCollection 생성

도형의 색상을 설정하고 `PatchCollection()`을 생성합니다.

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
