# 축 범위 설정 및 그림 저장

`io.BytesIO()` 및 `plt.savefig()`를 사용하여 축의 x 및 y 범위를 설정하고 그림을 SVG 형식의 바이트 문자열로 저장합니다.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
